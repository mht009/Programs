from machine import Pin
import time
for i in range(10):
    Pin(25, Pin.OUT).value(1)
    time.sleep(1)
    Pin(25, Pin.OUT).value(0)
    time.sleep(1)