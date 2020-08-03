#!/usr/bin/env python3
import time
import os
from datetime import datetime

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import board
import Adafruit_SSD1306
import adafruit_dht

FONT_SIZE = 14
data = {}

disp = Adafruit_SSD1306.SSD1306_128_64(rst=0)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

dhtDevice01 = adafruit_dht.DHT22(board.D4)
dhtDevice02 = adafruit_dht.DHT22(board.D18)

font = ImageFont.truetype(
    "/home/pi/PORTEX-ECM/etc/ARIALUNI.TTF", FONT_SIZE)
try:
    while True:
        temperature01 = dhtDevice01.temperature
        humidity01 = dhtDevice01.humidity
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((0, 0), 'DATE: {}'.format(
            time.strftime("%Y/%m/%d")),  font=font, fill=255)
        draw.text((0, FONT_SIZE-1),
                  'TIME:{}'.format(time.strftime("%H:%M:%S")), font=font, fill=255)
        draw.text((0, 2*FONT_SIZE-1),
                  'TEMP_01:{:0.2f}\xb0C'.format(temperature01),  font=font, fill=255)
        draw.text((0, 3*FONT_SIZE-1),
                  'HUM_01: {:0.2f}%'.format(humidity01),  font=font, fill=255)
        disp.image(image)
        disp.display()
        time.sleep(5)
        temperature02 = dhtDevice02.temperature
        humidity02 = dhtDevice02.humidity
        disp.clear()
        disp.display()
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((0, 0),
                  'TEMP_01:{:0.2f}\xb0C'.format(temperature01),  font=font, fill=255)
        draw.text((0, FONT_SIZE-1),
                  'HUM_01: {:0.2f}%'.format(humidity01),  font=font, fill=255)
        draw.text((0, 2*FONT_SIZE-1),
                  'TEMP_02:{:0.2f}\xb0C'.format(temperature02),  font=font, fill=255)
        draw.text((0, 3*FONT_SIZE-1),
                  'HUM_02: {:0.2f}%'.format(humidity02),  font=font, fill=255)
        disp.image(image)
        disp.display()
        time.sleep(5)
        disp.clear()
        disp.display()
except KeyboardInterrupt:
    print('close program')
finally:
    disp.clear()
    disp.display()
