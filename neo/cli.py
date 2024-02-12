'''
This file contains the command line interface

Author: R. Thomas
Place: U. of Sheffield
Year: 2023-24
Licence: GPLv3
Pylint v3.0.3 score: 10
'''
import argparse
import unittest

def arguments(args):
    '''
    This function set up the command line interface

    Parameter
    ---------
    args      : list
                of argument given in the command line

    Return
    ------
    options     :   Namespace
                    with argument analysed
    '''
    parser = argparse.ArgumentParser(prog='neo',
                                     description='This small program read a skills matrix and'+\
                                                 ' allows you to plot the skills matrices at'\
                                                 ' the group and individual levels')
    parser.add_argument('-m', '--matrix', type=str, help='Spreadsheet you want to open')
    parser.add_argument('-s', '--sheets', action='store_true',
                        help='List all sheets available in the file')
    parser.add_argument('-n', '--name', type=str,
                        help='Name of the sheet (sub skill matrix) to consider')
    parser.add_argument('-f', '--first', type=int,
                        help='First row of the matrix in the spreadsheet', default=2)
    parser.add_argument('-c', '--column', type=str, help='Letter of the Skill column', default='A')
    parser.add_argument('-e', '--rse', type=str,
                        help='Name of the rse to plot the skill matrix for')
    parser.add_argument('-t', '--training', action='store_true')
    parser.add_argument('--test', action='store_true', help='Run the test suite')

    options = parser.parse_args(args)

    return options


class TestArguments(unittest.TestCase):
    '''
    This test the argument function that builts that command line
    interface.
    '''

    def test_arguments(self):
        '''
        Test a standard configuration
        '''
        test_args = ['-m', 'example.xlsx', '-s', '-n', 'sub_skill_matrix',
                     '-f', '3', '-c', 'B', '-e', 'JohnDoe', '-t']
        options = arguments(test_args)

        self.assertEqual(options.matrix, 'example.xlsx')
        self.assertTrue(options.sheets)
        self.assertEqual(options.name, 'sub_skill_matrix')
        self.assertEqual(options.first, 3)
        self.assertEqual(options.column, 'B')
        self.assertEqual(options.rse, 'JohnDoe')
        self.assertTrue(options.training)
        self.assertFalse(options.test)

    def test_arguments_2(self):
        '''
        Another configuration
        '''
        test_args_2 = ['-m', 'another_example.xlsx', '-n', 'specific_sheet', '-e', 'JaneDoe']
        options_2 = arguments(test_args_2)

        self.assertEqual(options_2.matrix, 'another_example.xlsx')
        self.assertFalse(options_2.sheets)  # Not using -s in this case
        self.assertEqual(options_2.name, 'specific_sheet')
        self.assertEqual(options_2.first, 2)  # Assuming the default value for -f is 2
        self.assertEqual(options_2.column, 'A')  # Assuming the default value for -c is 'A'
        self.assertEqual(options_2.rse, 'JaneDoe')
        self.assertFalse(options_2.training)
        self.assertFalse(options_2.test)

    def test_arguments_3(self):
        '''
        test default values
        '''
        test_args = []
        options = arguments(test_args)

        # Assuming you have default values for some arguments
        self.assertIsNone(options.matrix)
        self.assertFalse(options.sheets)
        self.assertEqual(options.name, None)
        self.assertEqual(options.first, 2)
        self.assertEqual(options.column, 'A')
        self.assertIsNone(options.rse)
        self.assertFalse(options.training)
        self.assertFalse(options.test)
