import time
import adafruit_dht
import RPi._GPIO as gpio
import dht11
import datetime



gpio.setmode(gpio.BCM)

dhtlib = dht11.DHT11(pin = 17)

try:
    while True:
        result = dhtlib.read()
        if result.is_valid():
            current_time = datetime.datetime.now()
            print('Temperature is: ', result.temperature, 'Humidity is: ', result.humidity, 'Time is: ', current_time)
            exec(open("runTest.py").read())

        time.sleep(5)
except KeyboardInterrupt:
    gpio.cleanup()
    