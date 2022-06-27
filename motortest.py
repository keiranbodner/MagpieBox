import RPi.GPIO as GPIO

BEAM_OFF= 21
BEAM_ON= 20

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
