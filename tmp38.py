import plotly.plotly as py
import json
import time
import readadc
import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.celanup()
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26,1)
tempHI = 19.0
tempLOW = 17.0
host = '192.168.42.68'

with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

url = py.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': plotly_user_config['plotly_streaming_tokens'][0],
            'maxpoints': 200
        }
    }], filename='Raspberry Pi Streaming Example Values')

print "View your streaming graph here: ", url

# temperature sensor middle pin connected channel 0 of mcp3008
sensor_pin = 0
readadc.initialize()

stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()

#the main sensor reading and plotting loop
while True:
    sensor_data = readadc.readadc(sensor_pin,
                                  readadc.PINS.SPICLK,
                                  readadc.PINS.SPIMOSI,
                                  readadc.PINS.SPIMISO,
                                  readadc.PINS.SPICS)

    millivolts = sensor_data * (3300.0 / 1024.0)
    # 10 mv per degree
    temp_C = ((millivolts - 100.0) / 10.0) - 40.0
     # convert celsius to fahrenheit
    temp_F = (temp_C * 9.0 / 5.0) + 32
    # remove decimal point from millivolts
    millivolts = "%d" % millivolts
    # show only one decimal place for temprature and voltage readings
    temp_C = "%.1f" % temp_C
    temp_F = "%.1f" % temp_F
    stream.write({'x': datetime.datetime.now(), 'y':temp_C})
    time.sleep(5)
while True:	
    if (temp_C) > tempHI:
        GPIO.output(26,1) #turn GPIO pin 21 on
    elif (temp_C) < tempLOW:
        GPIO.output(26,0) #Turn GPIO pin 21 off
    time.sleep(10)
    GPIO.cleanup()
GPIO.output(26,0)
run(host=host, port=80)
    # write the data to plotly
   # stream.write({'x': datetime.datetime.now(), 'y': temp_C})
	
    # delay between stream posts
    #time.sleep(0)
