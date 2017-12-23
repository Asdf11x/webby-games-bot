#!/usr/bin/env python

"""botty.py: source code of sushi bot"""

import win32api, win32con, time

__author__      = "Asdf"
__copyright__   = "Copyright 2017, Planet Earth"


# global values for screen size on 130% zoom, get top right corner for x_pad and y_pad
# top left (x,y): 317, 292 and bot right (x,y): 1151, 917
x_pad = 317
y_pad = 292

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click.")          # completely optional. But nice for debugging purposes.


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print('left Down')


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print('left release')


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)


def startGame():
    # location of first menu - Play
    mousePos((420, 270))
    leftClick()
    time.sleep(.1)

    # location of second menu - Iphone continue
    mousePos((410, 510))
    leftClick()
    time.sleep(.1)

    # location of third menu - Skip
    mousePos((760, 595))
    leftClick()
    time.sleep(.1)

    # location of fourth menu
    mousePos((410, 500))
    leftClick()
    time.sleep(.1)


startGame()
