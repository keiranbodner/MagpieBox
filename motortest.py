import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

#Warnings are annoying
GPIO.setwarnings(False)

#Using GPIO Pins 23,24,25 which connect to Motor Controller
En,In1,In2 = 23,24,25
GPIO.setup(En,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)

#Pulse Width Modulation should be around 100hz, 1000 sounded really bad on our little motor
pwm = GPIO.PWM(En, 100)
pwm.start(0)

#We want a code like this to be able to be triggered by one breakbeam sensor and turned off by another
while True:
    #clockwise direction, medium rotational speed
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm.ChangeDutyCycle(50)
    sleep(5)
    #after five seconds goes to high speed
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm.ChangeDutyCycle(100)
    sleep(5)
#This code is not exactly what we want. We want the motor to turn on in a medium mode until the food sensor detects food, which is to turn the motor off.
#If food doesn't trip our sensor (because it is jammed in the hopper somehow), we want the motor to go to high, after maybe 3 seconds.
