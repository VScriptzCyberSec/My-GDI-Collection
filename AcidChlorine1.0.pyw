import win32gui
import win32con
import ctypes
import math
import time

try:
    import pywintypes
except ImportError:
    pass  # Handle the import error if pywintypes is not available

# Get the desktop handle and system metrics
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
sw, sh = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
hdc = win32gui.GetDC(0)

dx = dy = 1
angle = 0
size = 1
speed = 5

while True:
    try:
        win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY)
        dx = math.ceil(math.sin(angle) * size * 10)
        dy = math.ceil(math.cos(angle) * size * 10)
        angle += speed / 10
        angle = (angle + math.pi) % (2 * math.pi) - math.pi
    except pywintypes.error as e:
        # Handle specific error
        print(f"Error: {e}")
        # Optionally re-acquire the handle or handle the error appropriately
        time.sleep(1)  # Wait before retrying or exiting the loop

    time.sleep(0.01)  # Adjust sleep time as needed
