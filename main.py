import tkinter as tk
import threading
from utils import prevent_sleep, move_mouse

# Global variable for thread control
running = False

def start_script():
    global running
    running = True
    prevent_sleep()
    status_label.config(bg="green")
    threading.Thread(target=move_mouse, args=(running,)).start()

def stop_script():
    global running
    running = False
    status_label.config(bg="red")
    print("Script paused")

# Functions to make the window draggable
def start_move(event):
    global x, y
    x = event.x
    y = event.y

def stop_move(event):
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

# Status label to indicate running state
status_label = tk.Label(root, text="Status", bg="red", width=10)
status_label.pack(pady=10)

root.mainloop()
