import picamera
import os
import shelve
from time import sleep
from os.path import expanduser
from gi.repository import GExiv2
import BwDrone

camera = picamera.PiCamera()

def setupFolders():
    home = expanduser("~");
    missionFolder = home + "/missions"
    missionNumberFile = missionFolder + "/missionNumber.dat"
    number = 0
    
    if(os.path.isdir(missionFolder) == False):
    	os.mkdir(missionFolder);
    	print("Created missions folder: " + missionFolder)
    
    if(os.path.exists(missionNumberFile) == False):
        f = shelve.open(missionNumberFile)
        f['number'] = number;
    else:
        f = shelve.open(missionNumberFile)
        number = f['number']
        number = number+1;
        f['number'] = number;
    
    print("Current mission: " + str(number));
    f.close();
    currMissionFolder = missionFolder + "/" + str(number)
    os.mkdir(currMissionFolder);
    return currMissionFolder
	

def getPicture(folder, i):
    image = folder + "/" + str(i) + ".jpg"
    camera.capture(image)
    return image

def addExifData(image, position):
    exif = GExiv2.Metadata(image)
    exif.set_gps_info(position.lon, position.lat, position.alt)
    exif.save_file()

path = setupFolders();
print("Writing to " + path)
i = 0;
drone = BwDrone.BwDrone()
drone.connect()
while(True):
    print("Take picture " + str(i))
    image = getPicture(path, i);
    position = drone.getPosition()
    addExifData(image, position)
    sleep(3);
    i = i + 1;

