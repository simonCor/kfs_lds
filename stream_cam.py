#!/usr/bin/env python

import subprocess
import socket
import thread
import sys
import picamera
import kfs_cmd
import kfs_socket
from daemonize import Daemonize

host = "192.168.178.36" #macbook air on local network
#host = "192.168.178.24" #thoughpad on local network
stream_port = 8888
cmd_port = 8889
pid = "/tmp/test.pid"

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
	s = kfs_socket.Kfs_socket(host = host, port = stream_port, family = socket.AF_INET,
		type = socket.SOCK_STREAM)
	return s

def start_stream(stream_socket, cmd_socket, camera):
	camera.start_recording(stream_socket, format='h264')
	while(1):
		camera.wait_recording(60)
	camera.stop_recording()



def establish_connection():
	while(1):
		try:
			cs = connect_command_socket()
			ss = connect_stream_socket()
			break
		except(socket.error):
			print("error: connection failed")
			continue
	return(ss, cs)

def main():
	(ss, cs) = establish_connection()
	camera = picamera.PiCamera(resolution=(1920, 1080))

	st = thread.start_new_thread(start_stream, (ss, cs, camera))

	cmdl = kfs_cmd.Kfs_cmd(socket = cs, camera = camera)
	st = thread.start_new_thread(cmdl.start_command_interface, (ss,))

daemon = Daemonize(app="test_app", pid=pid, action=main)
daemon.start()
