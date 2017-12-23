#!/usr/bin/env python

"""quickGrab.py: Grab a screen from resolution 1920 x 1080 px mozilla firefox 130% zoom."""

import PIL.ImageGrab as ImageGrab
import os
import time

__author__      = "Asdf"
__copyright__   = "Copyright 2017, Planet Earth"


# global values for screen size on 130% zoom
# get top right corner for x_pad and y_pad
# top left (x,y): 317, 292 and bot right (x,y): 1151, 917
x_pad = 317
y_pad = 292


def screenGrab():
    """
    Use global values as corner top left start coordinates and add self measured screen size of the sushi game
    :return: None
    """
    box = (x_pad, y_pad, x_pad + 834, y_pad + 625)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def main():
    screenGrab()


if __name__ == '__main__':
    main()