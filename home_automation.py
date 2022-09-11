from distutils.cmd import Command
from filecmp import clear_cache
import os
from pydoc import cli
import queue
from time import sleep
from unicodedata import name
from pyautogui import click
from keyboard import press_and_release
from keyboard import press
from keyboard import write
from time import sleep
import time

from k2 import speak, takeCommand

def Activate(command):
     print(command)
     try:

          os.system('TASKKILL /F /im HD-Player.exe')
     except Exception as e:
          print(e)

     speak("Activating The Home Automation setup")

     press_and_release('win + m')


     os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\BlueStacks 5.lnk')

     sleep(2)

     press_and_release('win + up')

     sleep(20)

     click(x=205, y=661)

     sleep(40)

     # click(x=573, y=1055)

     click(x=757, y=357)

     while True:
          speak(f"Sir is it turned {command}?")
          query=takeCommand().lower()
          if 'yes' in query:
               speak(f"Ok Sir I successfully truned {command}!")
               break
          elif 'no' in query:
               click(x=757, y=357)

















