import ctypes
import pyautogui
import time
import random

# Constants for MS Windows API
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def prevent_sleep():
    print("Preventing from sleep Calling SetThreadExecutionState.")
    result = ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )
    if result == 0:
        print("Failed to set execution of state")
    else:
        print("Execution state set successfully")

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
        
        print('Pressing Alt + Tab')
        pyautogui.hotkey('alt', 'tab')
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
