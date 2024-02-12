'''
This file is part of Neo.
It is the entry point to the interface.


Author: R. Thomas
Year: 2023-24
Place: U. of Sheffield
Licence: GPLv3
Pylint: 10
'''


import os
import sys
import openpyxl

from . import cli
from . import meta_func
from . import hardcoded
from . import tests

def main():
    '''
    This is the main function of the program.
    It allows you to call the program from a terminal
    and then use the argument to display results of the call
    '''

    ##analyse arguments passed to the command
    args = cli.arguments(sys.argv[1:])
    print(args)

    ##analyse the arguments
    ##0-check if we run tests
    if args.test:
        print(hardcoded.BOLD + 'Run tests')
        tests.test()
        print(hardcoded.BOLD + '...exit..')
        sys.exit()

    ##1-first we must check if a file was given
    if args.matrix is None:
        print(hardcoded.BOLD + 'No spreadsheet was given....exit...')
        sys.exit()

    ##2-if it was given we must check that the file exist
    elif not os.path.isfile(args.matrix):
        print(hardcoded.BOLD + 'Spreadsheet not found....exit....')
        sys.exit()

    else:
        print(hardcoded.BOLD + 'Spreadsheet found...start analysis...')

    ###3-check if you want to display a sheets
    if args.sheets is True:
        ###open the matrix
        print(hardcoded.BOLD + 'Open file...')
        opened = openpyxl.load_workbook(args.matrix)
        print(hardcoded.BOLD_LIST + 'Extracting sheets...')
        for s in opened.sheetnames:
            print(hardcoded.BOLD_LIST + f'{s}')

    ###4-check if training
    elif args.training:
        print(hardcoded.BOLD + 'Extract training matrix...')
        meta_func.training_matrix(args.matrix)

    ###check single rse
    elif args.rse is None and args.name is not None:
        print(hardcoded.BOLD + f'Extracting {args.name} matrix')
        meta_func.single_matrix(args.matrix, args.name, args.first, args.column)

    ###check single rse
    elif args.rse is not None and args.name != 'all':
        print(hardcoded.BOLD + f'Extracting {args.name} matrix')
        meta_func.single_rse(args.matrix, args.name, args.first, args.column, args.rse)

    ###nothing has been requested
    else:
        print(hardcoded.BOLD + 'Nothing has been requested...exit...')

    ####End
    print(hardcoded.BOLD + 'End of request')
