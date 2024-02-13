import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.OUT)
gpio.output (20, 1)
time.sleep(0.5)
gpio.output (20, 0)
time.sleep(0.5)
gpio.output (20, 1)
time.sleep(0.5)
gpio.output (20, 0)
time.sleep(0.5)
gpio.output (20, 1)
time.sleep(0.5)
gpio.output (20, 0)
time.sleep(0.5)
gpio.output (20, 1)
time.sleep(0.5)
gpio.output (20, 0)
time.sleep(0.5)
gpio.output (20, 1)
