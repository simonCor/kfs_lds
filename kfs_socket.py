import socket

class Kfs_socket():
	def __init__(self, host, port, filename = "video.h264", family = socket.AF_INET, 
			type = socket.SOCK_STREAM, proto = 0):
		self.filename = filename
		self.filehandle = open(str(self.filename), "w")
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((host, port))

	def __del__(self):
		self.filehandle.close()
		self.socket.close()

	def send(self, string, flags=0):
		self.filehandle.write(string)
		self.socket.send(string, flags)
		self.flush()

	def write(self, string):
		self.send(string)

	def flush(self):
		self.filehandle.flush()