import socket
import pickle
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
import ast
import sys

reader = SimpleMFRC522()

def client_program():
	host = "motepi.local"  # as both code is running on same pc
	port = 5000  # socket server port number
	while True:
		try:
			client_socket = socket.socket()  # instantiate
			client_socket.connect((host, port))  # connect to the server
			while True:
				try:
					print("Waiting for card")
					id, text = reader.read()
					print(text)
					if text.strip() == "rainbow":
						print("rain")
						color = pickle.dumps(text)
					else:
                                		color = pickle.dumps(ast.literal_eval(text))
					a=10
					color = bytes(f'{len(color):<{a}}',"utf-8") + color
					print(color)
					client_socket.send(color)  # send message
				except KeyboardInterrupt:
					print("Closing")
				except:
					continue

			client_socket.close()  # close the connectio
		except KeyboardInterrupt:
			print("Closing")
		except:
			continue

if __name__ == '__main__':
	client_program()
