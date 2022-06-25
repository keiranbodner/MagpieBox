import time
import RPi.GPIO as GPIO
from picamera import PiCamera
from datetime import datetime
from openpyxl import load_workbook

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

start_time = time.time()

wb = load_workbook('/home/pi/Documents/Battery_Test_lithium.xlsx')
sheet = wb['Sheet1']

camera = PiCamera()
camera.resolution = (1280,760)
camera.framerate = 25

time.sleep(3)
moment = datetime.now()
camera.start_recording('/home/uleth/Videos/video_%02d_%02d_02d.mjpg' % (moment.hour, moment.minute, moment.second))
sleep(10)
camera.stop_recording()

while True:
    count_AA = 0
    while count_AA < 10:
        count_BB = 0
        while count_BB < 5:
            GPIO.output(7,True)
            time.sleep(0.5)
            GPIO.output(7,False)
            time.sleep(0.5)
            count_BB = count_BB + 1
        time.sleep(25)
        count_AA = count_AA + 1
    
    uptime = (time.time() - start_time) / 3600
    row = ('Uptime in Hours', uptime)
    sheet.append(row)
    
    wb.save('/home/pi/Documents/Battery_Test_lithium.xlsx')
    
message = input("Press enter to quit\n\n")
GPIO.cleanup()
