import time
import threading
from pyautogui import click
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener,KeyCode
import numpy as np
import pyautogui as pg
import cv2
TOGGLE_KEY = KeyCode(char="s")

clicking = False
mouse = Controller()


def Clicker():
    while True:
        if clicking:
            mouse.click(Button.left,2)
            # screenshot = pg.screenshot()
            # screenshot = cv2.cvtColor(np.array(screenshot),cv2.COLOR_RGB2BGR)
            # var = pg.locateOnScreen('Immagine.png')
            # if (var is not None):
            #     #mouse.move()
            #     mouse.move(var.left,var.top)
        time.sleep(0.00000001)


def ToggleEvent(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=Clicker)
click_thread.start()

with Listener(on_press=ToggleEvent) as listener:
    listener.join()