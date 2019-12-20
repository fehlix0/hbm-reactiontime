#Bot for https://www.humanbenchmark.com/tests/reactiontime - Run it, start the test and just leave it to run, average score: 89ms

import win32api, win32con
from PIL import ImageGrab
import pyscreenshot
import time

number = 1

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

while True:
    px=ImageGrab.grab().load()
    colour = px[691,482]
    if colour == (75,219,106):
       click(691,482)
       time.sleep(0.5)
       click(691,482)
