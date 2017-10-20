#! /usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

while True:
	GPIO.output(26, GPIO.HIGH)
	time.sleep(1)