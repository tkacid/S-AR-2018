#!/usr/bin/env python
# # -*- coding: utf-8 -*-

""" Simpple test for Scope AR
"""

import os
import colors
import time
import sys
import random


# raw_input returns the empty string for "enter"
yes = {'yes', 'y', 'ye', ''}
no = {'no', 'n'}


def makeflora(n):
    for i in range(n):
        print ' ' * (n - (i + 1)), '*' * (2*i+1)


def checkinput(l, h, number):

    if l <= number <= h:
        pass

    else:
        print "I said 20-30.... try again"
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
  Awesome Super Xmas Tree Maker! - Mike Dunham

				  """)


words()
toolbar_width = 30

# setup toolbar
sys.stdout.write("Shredding Cheese [%s]" % (" " * toolbar_width))
sys.stdout.flush()
# return to start of line, after '['
sys.stdout.write("\b" * (toolbar_width+1))

for i in xrange(toolbar_width):
    time.sleep(0.1)
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")

os.system('clear')

print("How big woud you like your tree?\n(Suggested 20-30): ")
tsize = int(raw_input().lower())
sizeresult = checkinput(20, 30, tsize)

print("Woah thats a little much, we just have one tree left, a old ragged nasty ascii tree.... Would you like it? (Yes | No)")

choice = raw_input().lower()

if choice in yes:
    os.system('clear')
    print "This is what you get and you better be happy with it:\n"
    makeflora(tsize)
    colors.prLightPurple("\n Merry Xmas by Michael Dunham\n")
elif choice in no:
    print "Try aagain but please respond with 'yes' or 'no'"
