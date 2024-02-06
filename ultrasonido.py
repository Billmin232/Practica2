from machine import Pin
import time

trigPin=Pin(5,Pin.OUT,0)
echoPin=Pin(18,Pin.IN,0)

soundVelocity=340
distance=0

def getSonar():
    trigPin.value(1)
    time.sleep_us(10)
    trigPin.value(0)
    while not echoPin.value():
        pass
    pingStart=time.ticks_us()
    while echoPin.value():
        pass
    pingStop=time.ticks_us()
    pingTime=time.ticks_diff(pingStop,pingStart)
    distance=pingTime*soundVelocity//2//10000
    return int(distance)

if __name__ == "__main__":
    time.sleep_ms(500)
    while True:
        time.sleep_ms(100)
        print('Distance: ',getSonar(),'cm' )
    