from machine import Pin,PWM
import time

class myServo(object):
    def __init__(self, pin: int=14, hz: int=50):
        self._servo = PWM(Pin(pin),hz) 
    
    def myServoWriteDuty(self, duty):
        if duty <= 26:
            duty = 26
        if duty >= 128:
            duty = 128
        self._servo.duty(duty)
        
    def myServoWriteAngle(self, pos):
        if pos <= 0:
            pos = 0
        if pos >= 180:
            pos = 180
        pos_buffer=(pos/180)*(128-26)
        self._servo.duty(int(pos_buffer)+26)

    def myServoWriteTime(self, us):
        if us <= 500:
            us = 500
        if us >= 2500:
            us = 2500
        pos_buffer=(1024*us)/20000
        self._servo.duty(int(pos_buffer))
        
    def deinit(self):
        self._servo.deinit()

servo = myServo(14)#set servo pin
servo.myServoWriteAngle(90)#Set Servo Angle
time.sleep_ms(1000)


if __name__ == "__main__":
    while True:       
        for i in range(90,180,1):
            servo.myServoWriteAngle(i)
            time.sleep_ms(15)
        for i in range(180,90,-1):
            servo.myServoWriteAngle(i)
            time.sleep_ms(15)  