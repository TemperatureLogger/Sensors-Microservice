import Adafruit_DHT
import random
import time
import json
import sys
import requests
import math

#Unique Device Serial Number
DEVICE_SERIAL = 111111

#Middle server URL
url = 'http://157.245.65.94:3000/api/measurements'

#Probing frequency
probe_freq = 2

#Sensor temperature reads limits
MIN_TEMP_CELSIUS = 0.0
MAX_TEMP_CELSIUS = 50.0

#Sensor humidity reads limits
MIN_HUMIDITY_PERCENT = 20.0
MAX_HUMIDITY_PERCENT = 90.0

#Hardware specification
sensor = Adafruit_DHT.DHT22
DHT_PIN = 4

#Data
entries = []

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_PIN)
    # if humidity is not None and temperature is not None:
    #     print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    # else:
    #     print("Failed to retrieve data from humidity sensor")

    #init new dictionary
    entry = {}

    #get dummy read
    tstamp = math.trunc(time.time())
    temperature = random.uniform(MIN_TEMP_CELSIUS, MAX_TEMP_CELSIUS)
    humidity = random.uniform(MIN_HUMIDITY_PERCENT, MAX_HUMIDITY_PERCENT)

    #add to dictionary
    entry['time'] = tstamp
    entry['temperature'] = temperature
    entry['humidity'] = humidity
    entry['serialNumber'] = DEVICE_SERIAL

    print(entry)
    # Send generated data to middle server
    x = requests.post(url, json = entry)
    print(x)
    if x.status_code is not 200:
        print("Server Error!")

    # wait desired amount of time
    time.sleep(probe_freq)
