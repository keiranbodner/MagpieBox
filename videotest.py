from picamera import PiCamera
import time
from datetime import datetime

camera = PiCamera()
camera.resolution = (1280,720)
camera.framerate = 25

time.sleep(3)
moment = datetime.now()
camera.start_recording('/home/uleth/Videos/video_%02d_%02d_%02d.mjpg' % (moment.hour, moment.minute, moment.second))
sleep(10)
camera.stop_recording()

message = input("Press enter to quit\n\n")
GPIO.cleanup()
