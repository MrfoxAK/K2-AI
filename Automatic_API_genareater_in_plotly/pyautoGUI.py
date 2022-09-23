from tokenize import Triple
from turtle import position
import pyautogui
from time import sleep
import win32api
from win32con import *
import webbrowser
from pyautogui import click
from keyboard import press_and_release
from keyboard import press
from keyboard import write
from pyautogui import tripleClick
# pyautogui.moveRel(0, 100, duration = 1)
# sleep(2)
# pyautogui.dragRel(100, 0, duration = 2)
#Scroll one down
# win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, -1, 0)


# for min
press_and_release('win + m')

webbrowser.open("https://chart-studio.plotly.com/settings/subscription")

sleep(1)
# for full screen
press_and_release('win + up')
sleep(5)
# api keys
click(x=88, y=803)
# for scroll
pyautogui.scroll(-150)
sleep(2)
# regenerate key
click(x=460, y=856)
sleep(1)
click(x=848, y=547)
sleep(1)

write("Akash@2002")

sleep(1)

click(x=948, y=652)

sleep(1)

tripleClick(x=729, y=790)

# pyautogui.dragTo(x=729, y=790,duration=2)

press_and_release('ctrl + c')


