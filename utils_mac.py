import pyautogui
import time
import random
import subprocess


# Prevent System Sleep/Lock
def prevent_sleep():
    print("Preventing system from sleeping using caffeinate.")
    subprocess.Popen(["caffeinate"])


def move_mouse():
    while True:
        print("Running...")
        pyautogui.moveRel(random.randint(5, 30), random.randint(5, 15))
        print("Moved")
        time.sleep(random.randint(5, 15))
        pyautogui.moveRel(random.randint(-20, -5), random.randint(-15, -5))
        print("Moved")
        time.sleep(random.randint(5, 15))

        print("Pressing Command + Tab")
        pyautogui.hotkey("command", "tab")
        time.sleep(random.randint(5, 10))

        pyautogui.moveRel(random.randint(10, 30), random.randint(5, 15))
        time.sleep(random.randint(1, 5))
        pyautogui.moveRel(random.randint(-15, -5), random.randint(-15, -5))
        time.sleep(random.randint(1, 5))
        pyautogui.moveRel(random.randint(10, 30), random.randint(5, 15))
        time.sleep(random.randint(1, 5))
        pyautogui.moveRel(random.randint(-25, -5), random.randint(-15, -5))
        print("Moved")


if __name__ == "__main__":
    prevent_sleep()
    move_mouse()
