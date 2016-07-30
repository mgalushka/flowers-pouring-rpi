import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

class ServoControl:
    def __init__(self):
      self.pwm = GPIO.PWM(18, 100)
      self.pwm.start(5)

    def updateAngle(self, angle):
        pwm.ChangeDutyCycle(angle)

if __name__ == '__main__':
    servo = ServoControl()
    servo.updateAngle(int(sys.argv[1]))
