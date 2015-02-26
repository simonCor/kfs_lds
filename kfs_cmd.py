import cmd
import picamera

class Kfs_cmd(cmd.Cmd):
	def __init__(self, socket, camera):
		self.use_rawinput = False
		file_socket = socket.makefile()
		cmd.Cmd.__init__(self, completekey = 'Tab', stdin = file_socket, 
			stdout=file_socket)
		self.stdin = file_socket
		self.stdout = file_socket
		self.camera = camera

	def do_help(self, s):
		self.stdout.write("Hi iam help\n")

	def do_brightness(self, level):
		"""brightness [level]
		set brightness level"""
		self.stdout.write("Hi iam brightness. " + level + "\n")
		try:
			self.camera.brightness = int(level)
		except picamera.exc.PiCameraValueError as e:
			self.stdout.write(e + "\n")


