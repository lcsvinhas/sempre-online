import ctypes
import time

mouse_event = ctypes.windll.user32.mouse_event

MOUSE_LEFTDOWN = 0x02
MOUSE_LEFTUP = 0x04

while True:
    time.sleep(60)
    mouse_event(MOUSE_LEFTDOWN, 0, 0, 0, 0)
    mouse_event(MOUSE_LEFTUP, 0, 0, 0, 0)
    print("Clique realizado!")
