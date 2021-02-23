#Imports
import time
import win32api
import win32con
import keyboard

#Prints the text
print("What delay do you want? (in seconds)")
#Colects the user information and makes it a float
seconds_delay = float(input())
#If delay equals 0 it set it to 0.00001 because 0 its to quick and not registers as clicks
if seconds_delay == 0:
    seconds_delay = 0.00001

#Waits 5 seconds before starting
time.sleep(5)

#While statement when q is pressed it stops the aplications
while keyboard.is_pressed('q') == False:
    #Basicly holds down click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #Delay of click
    time.sleep(seconds_delay)
    #Basicly stops holding click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
