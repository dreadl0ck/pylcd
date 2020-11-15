import lcd, time

lcd.lcd_init()
seconds = 0

while True:
    try:
        time.sleep(1)
        seconds += 1
        print(seconds)
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        lcd.lcd_string(seconds, 2)
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        lcd.lcd_string("seconds", 2)
    except KeyboardInterrupt:
        lcd.GPIO.cleanup()

