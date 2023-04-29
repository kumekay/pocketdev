#!/usr/bin/env python3
""" Battery voltage monitor """

import os
import time

from gpiozero import MCP3008, Button
from rpi_ws281x import PixelStrip, Color

DIVIDER = 5.1144

# ADC MCP3008
SPI_CLK = 15
SPI_MISO = 13
SPI_MOSI = 14
SPI_CS = 24
MCP3008_CH = 6

# LED
LED_COUNT = 1
LED_PIN = 12
LED_BRIGHTNESS = 100

# Button
BUTTON_PIN = 26

adc = MCP3008(
    channel=MCP3008_CH,
    clock_pin=SPI_CLK,
    mosi_pin=SPI_MOSI,
    miso_pin=SPI_MISO,
    select_pin=SPI_CS,
)

pixel = PixelStrip(LED_COUNT, LED_PIN, brightness=LED_BRIGHTNESS)
pixel.begin()


def battery_voltage() -> float:
    """Battery voltage"""
    return adc.value * DIVIDER


def get_color(voltage: float) -> Color:
    """Get color from voltage red -> green"""
    if voltage < 3.0:
        voltage = 3.0
    elif voltage > 4.2:
        voltage = 4.2

    r = int((4.2 - voltage) * 255 / 1.2)
    g = int((voltage - 3.0) * 255 / 1.2)
    b = 0

    return Color(r, g, b)

def set_pixel_color(color):
    pixel.setPixelColor(0, color)
    pixel.show()

def battery_status():
    voltage = battery_voltage()
    set_pixel_color(get_color(voltage))
    os.system(f'echo "Battery Voltage: {voltage:.2f}V" > /dev/kmsg')
    time.sleep(5)
    set_pixel_color(Color(0, 0, 0))

def shutdown():
    set_pixel_color(Color(0, 0, 255))
    os.system("shutdown -h now")


# User button
button = Button(26)
button.when_pressed = battery_status
button.hold_time = 10
button.when_held = shutdown


while True:
    time.sleep(15)
    if battery_voltage() < 3.4:
        battery_status()
