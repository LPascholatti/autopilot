import tkinter as tk
import threading
from utils import prevent_sleep, move_mouse

# Global event object for thread control
stop_event = threading.Event()

def start_script():
    stop_event.clear()  # Clear the event to allow the thread to run
    prevent_sleep()
    status_label.config(bg="green")
    # Start a new thread to run the move_mouse function
    threading.Thread(target=move_mouse, args=(stop_event,)).start()

def stop_script():
    stop_event.set()  # Set the event to stop the thread
    status_label.config(bg="red")
    print("Script paused")

def on_closing():
    stop_script()  # Ensure stopping the script when closing the app
    root.destroy()  # Destroy the Tkinter window

# Functions to make the window draggable
def start_move(event):
    global x, y
    x = event.x
    y = event.y

def stop_move(event):
    global x, y
    x = None
    y = None

def do_move(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    root.geometry(f"+{root.winfo_x() + deltax}+{root.winfo_y() + deltay}")

# Tkinter GUI
root = tk.Tk()
root.title("Auto Mouse Mover")

# Bind mouse events to make the window draggable
root.bind("<Button-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", do_move)

start_button = tk.Button(root, text="Start", command=start_script)
start_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause", command=stop_script)
pause_button.pack(pady=10)

info_label = tk.Label(root, text="Created by LPascholatti\nGitHub: https://github.com/LPascholatti/autopilot", font=("Arial", 10))
info_label.pack(pady=10)

# Status label to indicate running state
status_label = tk.Label(root, text="Status", bg="red", width=10)
status_label.pack(pady=10)

# Ensure that the script stops when the Tkinter window is closed
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
