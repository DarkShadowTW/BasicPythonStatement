import pyautogui
import keyboard

pyautogui.FAILSAFE = True

print("Press Ctrl-C to quit.")

count = 0
try:
    while True:
        count = count + 1
        print(count)
        if keyboard.is_pressed("ctrl+c"):
            print("KeyboardInterrupt")
            break
except KeyboardInterrupt:
    print("KeyboardInterrupt")