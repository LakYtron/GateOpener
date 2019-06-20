#!/usr/bin/python

import RPi.GPIO as GPIO
import time 
 # to use Raspberry Pi board pin numbers
# GPIO.setmode(GPIO.BOARD)

print("Garage Opener")
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)


GPIO.setup(17, GPIO.OUT)

print("UP!")
GPIO.output(17, GPIO.HIGH)


print("DOWN!")
GPIO.output(17, GPIO.LOW)


time.sleep(1)

print("UP!")
GPIO.output(17, GPIO.HIGH)


