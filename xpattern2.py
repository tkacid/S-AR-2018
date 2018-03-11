#!/usr/bin/env python
# # -*- coding: utf-8 -*-

""" Simpple test for Scope AR
"""

import os
import time
import sys
import random
import config


def make_da_x(s):

    for tx in range(s):
        p = list(" " * s)
        p[tx] = "*"
        p[-(tx+1)] = "*"
        print " ".join(p)


def loading_bar():

    # setup toolbar
    sys.stdout.write("Energizing Bananas [%s]" % (" " * config.toolbar_width))
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

    # Scope AR ASCII image
    prGreen("""\n
       _____                                 _____  
      / ____|                          /\   |  __ \ 
     | (___   ___ ___  _ __   ___     /  \  | |__) |
      \___ \ / __/ _ \| '_ \ / _ \   / /\ \ |  _  / 
      ____) | (_| (_) | |_) |  __/  / ____ \| | \ \ 
     |_____/ \___\___/| .__/ \___| /_/    \_\_|  \_\                        
          |_|
      --------------------------------------------
          Awesome Super X Maker! - Mike Dunham

          """)


def prGreen(skk):
    print("\033[92m {}\033[00m" .format(skk))


def main():

    # Dsiplays ACSII Scope AR text
    display_words()

    # Displays loading bar
    loading_bar()

    # Determines size of X
    print(config.eng_x_howbig)

    xsize = int(raw_input().lower())
    sizeresult = check_input(5, 20, xsize)

    if sizeresult:

        # Lets make our tree based off input size
        make_da_x(xsize)

    else:
        print(config.eng_error)


if __name__ == '__main__':
    sys.exit(main())
