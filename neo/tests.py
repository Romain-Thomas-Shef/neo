'''
This source code implements the tests for the module
To run the test just run skills --tests


Author: R. Thomas
Year: 2023-24
Place: U. of Sheffield
Licence: GPLv3
Pylint: 10
'''

##standard Library
import unittest

##third party libraries

#local imports
from . import hardcoded
from . import meta_func
from . import cli
from . import read_skills_matrix

def test():
    '''
    This function calls the test of each module and run them
    '''
    ###test the command line interface
    print(hardcoded.BOLD + 'Test the Command line interface')
    suite = unittest.TestLoader().loadTestsFromModule(cli)
    unittest.TextTestRunner(verbosity=2).run(suite)

    ###test the read_skills_matrix
    print(hardcoded.BOLD + 'Test the read_skills_matrix module')
    suite = unittest.TestLoader().loadTestsFromModule(read_skills_matrix)
    unittest.TextTestRunner(verbosity=2).run(suite)

    ###test the read_skills_matrix
    print(hardcoded.BOLD + 'Test the read_skills_matrix module')
    suite = unittest.TestLoader().loadTestsFromModule(meta_func)
    unittest.TextTestRunner(verbosity=2).run(suite)
