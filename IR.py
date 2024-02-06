from machine import Pin
import time

VolPin = Pin(25, Pin.IN, Pin.PULL_DOWN)

while True:
    if VolPin.value() == 1:
        print('Black')
    else:
        print('Other')
    time.sleep_ms(1000)
