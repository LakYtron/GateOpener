#!/usr/bin/python

import RPi.GPIO as GPIO
import time 
 # to use Raspberry Pi board pin numbers
# GPIO.setmode(GPIO.BOARD)

print("Gate Opener")
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)


GPIO.setup(18, GPIO.OUT)

print("UP!")
GPIO.output(18, GPIO.HIGH)


print("DOWN!")
GPIO.output(18, GPIO.LOW)


time.sleep(0.2)

print("UP!")
GPIO.output(18, GPIO.HIGH)


