import time
import win32api
import win32con
import keyboard

print("What delay do you want? (in seconds)")
seconds_delay = float(input())
if seconds_delay == 0:
    seconds_delay = 0.00001

time.sleep(5)

while keyboard.is_pressed('q') == False:
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(seconds_delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
