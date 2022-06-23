import time
import RPi.GPIO as GPIO
from openpyxl import load.workbook

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

start_time = time.time()

wb = load_workbook('/home/pi/Documents/Battery_Test.xlsx')
sheet = wb['Sheet1']

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
    
    wb.save('/home/pi/Documents/Battery_Test.xlsx')
    wb.save('/home/pi/Documents/Backup/Battery_Test.xlsx')