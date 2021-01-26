#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
from time import sleep

try:
	while True:
		r = input('Red:')
		g = input('Green:')
		b = input('Blue:')
		color = "(%s,%s,%s)" % (r, g, b)
		print("Now place your tag to write")
		reader.write(color)
		print("Written")
		sleep(2)
finally:
        GPIO.cleanup()
