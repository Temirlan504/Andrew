from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time
from images import clock, settings

WIDTH, HEIGHT = 128, 64 # Display dimensions
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000) # I2C on pins 0 and 1
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) # Display object

# Frame buffers (bytearray image, size_x, size_y, monochrome image)
fb = framebuf.FrameBuffer(clock, 48,48, framebuf.MONO_HLSB)
fb2 = framebuf.FrameBuffer(settings, 48,48, framebuf.MONO_HLSB)

oled.fill(0) # Fill display with nothing (1 is turn on all pixels). Reseting display

msg = "Hello, world"

while True:
    oled.text(msg, 0,0) # Load text to the display memory
    oled.show() # Show everything from the display memory
    
    time.sleep(1)
    
    oled.fill(0)
    oled.blit(fb, 0,0) # Load framebuff to the display memory (framebuff image, pos_x,pos_y)
    oled.show()
    
    time.sleep(1)
    
    oled.fill(0)
    oled.blit(fb2, 0,0) # Load framebuff to the display memory (framebuff image, pos_x,pos_y)
    oled.show()
    
    time.sleep(1)
    oled.fill(0)