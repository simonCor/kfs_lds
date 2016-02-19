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

	def start_command_interface(self, socket):
		while(1):
			self.cmdloop()

	def do_help(self, s):
		self.stdout.write("The followoing commands are available:\n")

	def help_brightness(self):
		print 'brightness [level] set brightness level'

	def do_brightness(self, level):
		"""brightness [level]
		set brightness level"""
		try:
			self.camera.brightness = int(level)
			self.stdout.write("done\n")
		except picamera.exc.PiCameraValueError as e:
			self.stdout.write(str(e) + "\n")

	def do_res(self, res):
		'brightness [level] set brightness level'
		try:
			(x,y) = str.split(res)
			self.camera.resolution = (int(x), int(y))
			self.stdout.write("done\n")
		except picamera.exc.PiCameraValueError as e:
			self.stdout.write(str(e) + "\n")
