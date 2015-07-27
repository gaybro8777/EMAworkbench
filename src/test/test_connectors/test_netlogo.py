'''
Created on 18 mrt. 2013

@author: localadmin
'''
import os
import unittest

from expWorkbench import ParameterUncertainty, CategoricalUncertainty, Outcome
from connectors.netlogo import NetLogoModelStructureInterface

def setUpModule():
    global cwd 
    cwd = os.getcwd()
    dir_of_module = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dir_of_module)

def tearDownModule():
    os.chdir(cwd)

class PredatorPrey(NetLogoModelStructureInterface):
    model_file = r"/Wolf Sheep Predation.nlogo"
    
    run_length = 1000
    
    uncertainties = [ParameterUncertainty((10, 100), "grass-regrowth-time"),
                     CategoricalUncertainty(("true", "false"), "grass?") ]
    
    outcomes = [Outcome('sheep', time=True),
                Outcome('wolves', time=True)]

class Test(unittest.TestCase):

    def test_init(self):
        wd = r"../models"
        
        PredatorPrey(wd, "predPreyNetlogo")
        
    def test_run_model(self):
        wd = r"../models"
        
        model = PredatorPrey(wd, "predPreyNetlogo")
        model.model_init({'name':'no policy'}, None)
        
        case = {"grass-regrowth-time": 35,
                "grass?": "true"}
        
        model.run_model(case)
        _ =  model.retrieve_output()

        model.cleanup()
        

if __name__ == "__main__":
    unittest.main()
