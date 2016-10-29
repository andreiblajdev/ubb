import os
import operator

from cmd import *
from ui import *
from tests import *

def main():

    os.system('clear') # CLEAR SCREEN

    undo_steps = []

    categoryList = buildCategList() # Default category list
    cmdList = buildCmdList()        # Default command list

    try:
        testEverything()
        print("All tests passed!")
    except Exception as ex:
        print(ex)
        exit(0)

    print("   Welcome!\n   Please choose the type of user interface:")
    print("   1. Command based.")
    print("   2. UI based.")
    UIType = raw_input("~: ")

    while UIType not in ['1', '2']:
        os.system('clear')
        print("   Invalid input.")
        print("   1. Command based.")
        print("   2. UI based.")
        UIType = raw_input("~: ")

    if UIType == '1':
        commandBased(categoryList, cmdList, undo_steps)
    else:
        UIBased(categoryList, cmdList, undo_steps) # to be implemented

if __name__ == '__main__':
    main()
