from myservo import myServo
import time

servo=myServo(14)#set servo pin
servo.myServoWriteAngle(90)#Set Servo Angle
time.sleep_ms(1000)

try:
    while True:       
        for i in range(90,180,1):
            servo.myServoWriteAngle(i)
            time.sleep_ms(15)
        for i in range(180,90,-1):
            servo.myServoWriteAngle(i)
            time.sleep_ms(15)        
except:
    servo.deinit()