#!/usr/bin/env python
# # -*- coding: utf-8 -*-

""" Simpple test for Scope AR
"""

import os
import time
import sys
import random
import config


def make_flora(n):

    # Make tree
    for i in range(n):
        print ' ' * (n - (i + 1)), '*' * (2*i+1)

    return True, n


def loading_bar():

    # setup toolbar
    sys.stdout.write("Shredding Cheese [%s]" % (" " * config.toolbar_width))
    sys.stdout.flush()

    # return to start of line, after '['
    sys.stdout.write("\b" * (config.toolbar_width+1))

    for i in xrange(config.toolbar_width):
        time.sleep(0.1)
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("\n")


def check_input(l, h, number):

    # Checks the input to see if its in range
    if l <= number <= h:
        return True
    else:
        return False


def display_words():
    
    #Scope AR ASCII image
    prGreen("""\n
       _____                                 _____  
      / ____|                          /\   |  __ \ 
     | (___   ___ ___  _ __   ___     /  \  | |__) |
      \___ \ / __/ _ \| '_ \ / _ \   / /\ \ |  _  / 
      ____) | (_| (_) | |_) |  __/  / ____ \| | \ \ 
     |_____/ \___\___/| .__/ \___| /_/    \_\_|  \_\                        
          |_|
      --------------------------------------------
      Awesome Super Xmas Tree Maker! - Mike Dunham

          """)

def prGreen(skk): 
    print("\033[92m {}\033[00m" .format(skk))


def main():

    # Dsiplays ACSII Scope AR text
    display_words()

    # Displays loading bar
    loading_bar()

    # Determines size of tree based off user input
    print(config.eng_howbig)
    tsize = int(raw_input().lower())
    sizeresult = check_input(20, 30, tsize)

    if sizeresult:
        # Asks the users if they would like to proceed with their tree
        print(config.eng_txtree)
        choice = raw_input().lower()

        if choice in config.yes:

            # Lets make our tree based off input size
            make_flora(tsize)

            # Display thank you message
            print(config.eng_thankyou)

        elif choice in config.no:
            print(config.eng_yorn)

    else:
        print(config.eng_error)


if __name__ == '__main__':
    sys.exit(main())
