from machine import Pin
import time
from ultrasonido import getSonar
from myservo import myServo

servo = myServo(14)#set servo pin
servo.myServoWriteAngle(0)#Set Servo Angle
time.sleep_ms(1000)

if __name__ == "__main__":
    
    try:
        while True:
            distanica = getSonar()
            print("Distance:", getSonar())
            if getSonar() <= 50:
                angulo = (getSonar()/50) * 180
                print("Angulo:", angulo)
                servo.myServoWriteAngle(angulo)
            elif getSonar() > 50:
                print("Demasiada distancia")
                while getSonar() > 50:
                    time.sleep_ms(100)
            time.sleep_ms(50)
    except:
        servo.deinit()