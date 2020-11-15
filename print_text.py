import lcd

lcd.lcd_init()
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
lcd.lcd_string("hello world", 2)

lcd.GPIO.cleanup()
