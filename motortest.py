import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

En,In1,In2 = 23,24,25
GPIO.setup(En,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)
pwm = GPIO.PWM(En, 100)
pwm.start(0)

variable = [1,2,3,4,5]


while True:
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm.ChangeDutyCycle(50)
    sleep(5)
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm.ChangeDutyCycle(100)
    sleep(5)
