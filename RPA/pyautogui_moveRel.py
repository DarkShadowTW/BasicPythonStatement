#移動滑鼠在所在座標

import pyautogui

for i in range(4):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)

for i in range(4):
    pyautogui.moveRel(100, 0)
    pyautogui.moveRel(0, 100)
    pyautogui.moveRel(-100, 0)
    pyautogui.moveRel(0, -100)