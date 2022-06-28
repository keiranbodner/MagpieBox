import RPi.GPIO as GPIO
import time

'''
######################
Define Constants and startup global variables.
######################
'''

# The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number, these are the numbers after "GPIO" in the green rectangles around the outside of the below diagrams:
# https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
GPIO.setmode(GPIO.BCM)

#Warnings are annoying
GPIO.setwarnings(False)


BEAM_OFF = 21 # pin 21 for Sensor to turn motor off
BEAM_ON = 20 # Pin 20 for Sensor to turn motor on

# Sets up GPIO pins 23 - 24 as output
En = 23
In1 = 24
In2 = 25

# write out on pin EN.
GPIO.setup(En,GPIO.OUT)

# Motor controls
# In1 is sending a low signal
GPIO.setup(In1,GPIO.OUT)
GPIO.output(In1, GPIO.LOW)

# In2 is sending a high signal
GPIO.setup(In2,GPIO.OUT)
GPIO.output(In2, GPIO.HIGH)

# PWM is initialized to pin 23 at 100HZ
motor_control = GPIO.PWM(En, 100) # GPIO.PWM(channel, frequency)

# NOTE about PWM and how it works https://resources.pcb.cadence.com/blog/2020-pulse-width-modulation-characteristics-and-the-effects-of-frequency-and-duty-cycle
#     Duty cycle: A duty cycle is the fraction of one period when a system or signal is active. We typically express a duty cycle as a ratio or percentage. A period is the time it takes for a signal to conclude a full ON-OFF cycle.
#     Frequency: The rate at which something repeats or occurs over a particular period. In other words, the rate at which a vibration happens that creates a wave, e.g., sound, radio, or light waves, typically calculated per second. 
#  
#  

STOP_MOTOR = False
'''
######################
Define Functions here.
######################
'''

# Bind whatever purpose you want into these functions.
# Callbacks are only called when an event has happened
# In this case you bind GPIO.BOTH so actions are called whether a state has been changed in either direction
# Example from HI to LO or Lo to HI


def motor_off_callback(channel):
    """
    A callback function when bound pin changes state
    """
    if GPIO.input(BEAM_OFF):
        print("beam1 unbroken")
    else:
        print("beam1 broken")
        STOP_MOTOR = True #Exit loop in other callback if neccisary
        motor_control.stop()
        


def motor_on_callback(channel):
    if GPIO.input(BEAM_ON):
        print("beam2 unbroken")

    else:
        print("beam2 broken")

        start = time.time() # Start time
        now = start

        motor_control.start(50) # Start with Duty Cycle at 50 

        # Instead of sleep, we use a while loop to test if time has been 5 seconds
        # I do this because sleep may interfere with the other callback.
        # If food drops before 5 seconds, we do not need to go to high speed, instead, the other callback is triggered and we stop.
        while now - start <= 5:
            now = time.time() # Update now.
            if GPIO.input(BEAM_OFF):
                pass
            else:
                motor_control.stop()
        # Will exit the loop here after 5 and continue if STOP_MOTOR has not been called.

        # after five seconds goes to high speed and set Duty Cycle to 100
        motor_control.ChangeDutyCycle(100)

        while GPIO.input(BEAM_OFF):
            continue

        motor_control.stop()

        # This will continue until motor_off callback is called and when sensor 1 is broken.
            


if __name__ == "__main__":

    # Bind GPIO to callback functions defined above
    # NOTE these are binding input signals to a function, you only need to do this once.
    print("Starting Sensors")


    GPIO.setup(BEAM_OFF, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.add_event_detect(BEAM_OFF, GPIO.BOTH, callback=motor_off_callback)

    GPIO.setup(BEAM_ON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BEAM_ON, GPIO.BOTH, callback=motor_on_callback)

    print("All sensors active.")

    # Run active indefinitely or else the program will end. 
    while True:
        continue
