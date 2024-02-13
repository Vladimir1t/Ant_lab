import RPi.GPIO as gpio
 
gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.OUT)
gpio.setup (25, gpio.IN)

gpio.output(20, gpio.input(25))
while True:
    