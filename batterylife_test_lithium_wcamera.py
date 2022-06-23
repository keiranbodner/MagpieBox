import time
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
from openpyxl import load_workbook

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

start_time = time.time()

wb = load_workbook('/home/pi/Documents/Battery_Test_lithium.xlsx')
sheet = wb['Sheet1']

camera = PiCamera()
camera.rotation = 180
camera.resolution = (1920,1080)
camera.framerate = 30

camera.start_preview()
camera.start_recording('/home/uleth/Videos/video.h264')
sleep(86400)
camera.stop_recording()
camera.stop_preview()

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