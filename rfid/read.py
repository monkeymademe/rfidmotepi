#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()

try:
	while True:
		print("Place card on reader")
		id, text = reader.read()
		print("------")
		print(id)
		print(text)
		print("------")
		sleep(5)
finally:
        GPIO.cleanup()
