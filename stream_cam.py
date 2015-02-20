#!/usr/bin/env python

import subprocess
import socket
from thread import start_new_thread
import sys
import picamera

host = "192.168.178.36"
port = 8888

def start_stream(socket):
	file_socket = socket.makefile('wb')
	with picamera.PiCamera(resolution=(1920, 1080)) as camera:
		camera.start_recording(file_socket, format='h264')
		while(1):
			camera.wait_recording(15)
		camera.stop_recording()


def establish_connection():
	global port
	global host
	s = socket.socket()
	while(1):
		try:
			s.connect((host, port))
			break
		except(socket.error):
			print("error: connection failed")
			continue
	return s

socket = establish_connection()
start_stream(socket)