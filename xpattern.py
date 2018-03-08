#!/usr/bin/env python
# # -*- coding: utf-8 -*-

""" Simpple test for Scope AR
"""

import os
import colors
import time
import sys
import random


def makedax(s):

    for tx in range(s):
        p = list(" " * s)
        p[t] = "*"
        p[-(tx+1)] = "*"
        print " ".join(p)


def checkinput(l, h, number):

    if l <= number <= h:
        pass

    else:
        print "I said 5-20.... try again"
        exit()


def words():
    colors.prGreen("""\n
   _____                                 _____  
  / ____|                          /\   |  __ \ 
 | (___   ___ ___  _ __   ___     /  \  | |__) |
  \___ \ / __/ _ \| '_ \ / _ \   / /\ \ |  _  / 
  ____) | (_| (_) | |_) |  __/  / ____ \| | \ \ 
 |_____/ \___\___/| .__/ \___| /_/    \_\_|  \_\                        
		  |_|
  --------------------------------------------
  Awesome X Pattern Maker! - Mike Dunham

				  """)


words()
toolbar_width = 30

# setup toolbar
sys.stdout.write("Energizing Bananas [%s]" % (" " * toolbar_width))
sys.stdout.flush()
# return to start of line, after '['
sys.stdout.write("\b" * (toolbar_width+1))

for i in xrange(toolbar_width):
    time.sleep(0.1)
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")

os.system('clear')

print("How big do you want your X?\n(Suggested 5-20): ")

xsize = int(raw_input().lower())
sizeresult = checkinput(5, 20, xsize)

os.system('clear')
makedax(xsize)
colors.prLightPurple("\nEnjoy your X Michael Dunham\n")
