import pyautogui
import time
import random
import subprocess


# Prevent System Sleep/Lock
def prevent_sleep():
    print("Preventing system from sleeping using caffeinate.")
    subprocess.Popen(["caffeinate"])


def move_mouse(stop_event):
    while not stop_event.is_set():
        print("Running...")
        pyautogui.moveRel(random.randint(5, 30), random.randint(5, 15))
        print("Moved")
        time.sleep(random.randint(5, 15))
        pyautogui.moveRel(random.randint(-20, -5), random.randint(-15, -5))
        print("Moved")
        time.sleep(random.randint(5, 15))

        if stop_event.is_set():  # Check periodically
            break

        print("Pressing Command + Tab")
        pyautogui.hotkey("command", "tab")
        time.sleep(random.randint(5, 10))

        if stop_event.is_set():  # Check periodically
            break

        pyautogui.moveRel(random.randint(10, 30), random.randint(5, 15))
        time.sleep(random.randint(1, 5))
        pyautogui.moveRel(random.randint(-15, -5), random.randint(-15, -5))
        time.sleep(random.randint(1, 5))
        pyautogui.moveRel(random.randint(10, 30), random.randint(5, 15))
        time.sleep(random.randint(1, 5))
        pyautogui.moveRel(random.randint(-25, -5), random.randint(-15, -5))
        print("Moved")

    print("Thread exiting...")
