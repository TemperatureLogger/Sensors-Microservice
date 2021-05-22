import Adafruit_DHT
import random
import time
import json
import sys
import requests
import math

#Middle server URL
url = 'http://157.245.65.94:3000/api/measurements'

#Probing frequency
probe_freq = 1#int(sys.argv[1])

#Sensor temperature reads limits
MIN_TEMP_CELSIUS = 0.0
MAX_TEMP_CELSIUS = 50.0

#Sensor humidity reads limits
MIN_HUMIDITY_PERCENT = 20.0
MAX_HUMIDITY_PERCENT = 90.0

#Hardware specification
sensor = Adafruit_DHT.DHT11
DHT11_pin = 23

#Data
entries = []
#{
#    "temperature":"1112.1312321",
#    "humidity": "7811111.123213"
#}


#GENERATE DUMMY DATA
while True:
    #init new dictionary
    entry = {}

    #get dummy read
    # tstamp = time.strftime("%Y-%d-%b %H-%M-%S")
    tstamp = math.trunc(time.time())
    temperature = random.uniform(MIN_TEMP_CELSIUS, MAX_TEMP_CELSIUS)
    humidity = random.uniform(MIN_HUMIDITY_PERCENT, MAX_HUMIDITY_PERCENT)

    #add to dictionary
    entry['tstamp'] = tstamp
    entry['temperature'] = temperature
    entry['humidity'] = humidity

    print(entry)
    # Send generated data to middle server
    x = requests.post(url, json = entry)
    print(x)
    if x.status_code is not 200:
        print("Server Error!")

    # wait desired amount of time
    time.sleep(probe_freq)

#UNCOMMENT WHEN SENSOR IS REPLACED

# humidity, temperature = Adafruit_DHT.read(sensor, DHT11_pin)
# 
# if humidity is not None and temperature is not None:
    # print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
# else:
    # print('Failed to get reading from the sensor. Try again!')
