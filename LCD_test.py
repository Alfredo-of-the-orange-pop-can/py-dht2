"""
import RPLCD

from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])
lcd.write_string(u'Hello world!')


import time
from LCD import LCD

# Initialize the LCD with specific parameters: Raspberry Pi revision, I2C address, and backlight status
lcd = LCD(2, 0x27, True)  # Using Raspberry Pi revision 2, I2C address 0x27, backlight enabled

# Display messages on the LCD
lcd.message("Hello World!", 1)        # Display 'Hello World!' on line 1
lcd.message("    - Sunfounder", 2)    # Display '    - Sunfounder' on line 2

# Keep the messages displayed for 5 seconds
time.sleep(5)

# Clear the LCD display
lcd.clear()

"""

"""Implements a HD44780 character LCD connected via MCP23008 on I2C."""

from pyb import I2C, delay, millis
from pyb_i2c_adafruit_lcd import I2cLcd

# The MCP23008 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x20

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    i2c = I2C(1, I2C.MASTER)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 4, 20)
    lcd.putstr("It Works!\nSecond Line\nThird Line\nFourth Line")
    delay(3000)
    lcd.clear()
    count = 0
    while True:
        lcd.move_to(0, 0)
        lcd.putstr("%7d" % (millis() // 1000))
        delay(1000)
        count += 1
        if count % 10 == 3:
            print("Turning backlight off")
            lcd.backlight_off()
        if count % 10 == 4:
            print("Turning backlight on")
            lcd.backlight_on()
        if count % 10 == 5:
            print("Turning display off")
            lcd.display_off()
        if count % 10 == 6:
            print("Turning display on")
            lcd.display_on()
        if count % 10 == 7:
            print("Turning display & backlight off")
            lcd.backlight_off()
            lcd.display_off()
        if count % 10 == 8:
            print("Turning display & backlight on")
            lcd.backlight_on()
            lcd.display_on()

#if __name__ == "__main__":
test_main()
