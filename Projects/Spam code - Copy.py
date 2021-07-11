from pynput.keyboard import Key, Controller
keyboard = Controller()

import time
x=1
time.sleep(2)

while x<100:
    time.sleep(0.1)
    keyboard.type ("i like eMath ")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    x=x+1
