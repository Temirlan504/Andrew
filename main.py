from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

WIDTH, HEIGHT = 128, 64 # Display dimensions

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000) # I2C on pins 0 and 1
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) # Display object

msg = "Hello, world!"

oled.fill(0) # Fill screen with nothing (1 is turn on all pixels)

oled.text(msg, 0,0) # Load text to the display memory
oled.show() # Show everything from the display memory