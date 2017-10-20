import RPi.GPIO as GPIO
import time	
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.IN)
t=0
GPIO.setup(19, GPIO.IN)
GPIO.setup(19, GPIO.OUT)

while True :
		input_state = GPIO.input(13)
		GPIO.output(19,False)
		time.sleep(0)