#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode (GPIO.BCM)
GPIO.setup (26, GPIO.OUT)
#GPIO.setup (15, GPIO.OUT)
#forward(3)
#sleep(0.5)
try:

 while True:
	GPIO.output(26, 1)
	sleep(0.5)

except KeyboardInterrupt:
 GPIO.cleanup()


