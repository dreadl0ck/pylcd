import lcd, time

lcd.lcd_init()
seconds = 0

while True:
    try:
        time.sleep(1)
        seconds += 1
        fmt = time.strftime('%H:%M:%S', time.gmtime(seconds))
        print(fmt)

        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        lcd.lcd_string(fmt, 2)
        
        #lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        #lcd.lcd_string("seconds", 2)
    except KeyboardInterrupt:
        lcd.GPIO.cleanup()
        exit(0)

