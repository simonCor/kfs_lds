#!/usr/bin/env python

import subprocess
import socket
import thread
import sys
import picamera
import kfs_cmd

host = "192.168.178.36" #macbook air on local network
#host = "192.168.178.24" #thoughpad on local network
stream_port = 8888
cmd_port = 8889

def connect_socket(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s

def connect_command_socket():
	global cmd_port
	global host
	return connect_socket(host, cmd_port)

def connect_stream_socket():
	global stream_port
	global host
	return connect_socket(host, stream_port)

def start_stream(stream_socket, cmd_socket):
	file_socket = stream_socket.makefile('wb')
	with picamera.PiCamera(resolution=(1920, 1080)) as camera:
		camera.start_recording(file_socket, format='h264')
		while(1):
			cmdl = kfs_cmd.Kfs_cmd(cmd_socket, camera)
			cmdl.cmdloop()
		camera.stop_recording()

def start_command_interface(socket, stream_thread):
	while(1):
		cmdl = kfs_cmd.Kfs_cmd(socket)
		cmdl.cmdloop()

def establish_connection():
	while(1):
		try:
			cs = connect_command_socket()
			ss = connect_stream_socket()
			break
		except(socket.error):
			#print("error: connection failed")
			continue
	return(ss, cs)


(ss, cs) = establish_connection()

st = thread.start_new_thread(start_stream, (ss, cs))

while(1):
	pass