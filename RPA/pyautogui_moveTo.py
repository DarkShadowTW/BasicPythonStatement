#移動滑鼠

import pyautogui

for i in range(4):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

for i in range(4):
    pyautogui.moveTo(100, 100)
    pyautogui.moveTo(200, 100)
    pyautogui.moveTo(200, 200)
    pyautogui.moveTo(100, 200)