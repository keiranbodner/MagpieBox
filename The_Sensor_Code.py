import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BEAM_OFF= 21
BEAM_ON= 20

En = 23
In1 = 24
In2 = 25

GPIO.setup(En,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.output(In1, GPIO.LOW)
GPIO.setup(In2,GPIO.OUT)
GPIO.output(In2, GPIO.HIGH)
motor_control = GPIO.PWM(En, 100)

def break_beam_callback(channel):
    if GPIO.input(BEAM_OFF):
        print("beam1 unbroken")
    else:
        print("beam1 broken")
        motor_control.stop()

def break_beam_callback1(channel):
    if GPIO.input(BEAM_ON):
        print("beam2 unbroken")
    else:
        print("beam2 broken")
        motor_control.start(15)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_OFF, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BEAM_OFF, GPIO.BOTH, callback=break_beam_callback)
GPIO.setup(BEAM_ON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BEAM_ON, GPIO.BOTH, callback=break_beam_callback1)
