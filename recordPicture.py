import picamera
import os
from os.path import expanduser


print(os.path.exists("/home/el/myfile.txt"))
def setupFolders():
    home = expanduser("~");
    print(os.path.isdir(home + "missions"))


camera = picamera.PiCamera()

camera.capture('image.jpg')
