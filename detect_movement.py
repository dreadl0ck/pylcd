import lcd

lcd.lcd_init()
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
lcd.lcd_string("movement detector v0.1", 2)

import RPi.GPIO as GPIO
import time, sys

# Wait for 3 seconds
time.sleep(3)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)         #Read output from PIR motion sensor
#GPIO.setup(3, GPIO.OUT)         #LED output pin

while True:
    try:
        i=GPIO.input(17)
        
        if i==0:                 # When output from motion sensor is LOW
            print("all quiet",i)
            lcd.lcd_string("all quiet", 2)
            #GPIO.output(3, 0)  #Turn OFF LED
            time.sleep(0.1)
        elif i==1:               # When output from motion sensor is HIGH
            print("movement detected",i)
            lcd.lcd_string("movement detected", 2)
            #GPIO.output(3, 1)  #Turn ON LED
            time.sleep(0.1)
    except KeyboardInterrupt:
        lcd.GPIO.cleanup()
