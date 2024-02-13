import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setup (26, gpio.OUT)
gpio.output (26,0)
