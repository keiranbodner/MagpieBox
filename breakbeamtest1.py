import RPi.GPIO as GPIO

#chose GPIO pin 21 for our food sensor, and GPIO 20 for object sensor. 
#Object sensor sets of motor, food sensor stops motor
BEAM_OFF= 21
BEAM_ON= 20

#not sure how this works, but we managed to get both sensors working individually with this code. We need 'beam1 broken' to signal motor to run
#'beam2 broken' is to signal motor to stop
def break_beam_callback(channel):
    if GPIO.input(BEAM_OFF):
        print("beam1 unbroken")
    else:
        print("beam1 broken")

def break_beam_callback1(channel):
    if GPIO.input(BEAM_ON):
        print("beam2 unbroken")
    else:
        print("beam2 broken")

GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_OFF, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BEAM_OFF, GPIO.BOTH, callback=break_beam_callback)
GPIO.setup(BEAM_ON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BEAM_ON, GPIO.BOTH, callback=break_beam_callback1)

message = input("Press enter to quit\n\n")
GPIO.cleanup()
