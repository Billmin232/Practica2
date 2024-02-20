"""Programa ESP33"""

from BLE import *
from UART import *
import time

sender = UartClass(1,4,5)

def on_rx(rx_data):
        print("RX", rx_data)
        sender.send_command(rx_data)

ble = bluetooth.BLE()
p = BLESimplePeripheral(ble)
p.on_write(on_rx)

while True:
    time.sleep_ms(1000)
    p.send("I'm alive")