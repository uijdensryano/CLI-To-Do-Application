#!/usr/bin/python3
import sys
import json


# to do application for use in the terminal
# functions
def get_flag_arguments(arguments_list, flag):
    print("temporary")


# main programm
arguments = sys.argv
arguments.pop(0)

if not arguments:
    # show to-do list
    print("temporary")
elif arguments.__contains__("-a"):
    # add new items
    arguments.pop(0)

    with open("to-do.json", "w", "UTF-8") as data:
        
