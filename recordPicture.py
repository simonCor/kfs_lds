import picamera
import os
import shelve
from time import sleep
from os.path import expanduser
from gi.repository import GExiv2
import BwDrone
import shutil
minFreeSpace = 500000000
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
    return(currMissionFolder, missionFolder, number)
	

def getPicture(folder, i):
    image = folder + "/" + str(i) + ".jpg"
    camera.capture(image)
    return image

def addExifData(image, position):
    exif = GExiv2.Metadata(image)
    exif.set_gps_info(position.lon, position.lat, position.alt)
    exif.save_file()

def checkDiskSpaceAndClean(baseFolder, currentMissionNumber):
    stat = os.statvfs(baseFolder)
    freeSpace = stat.f_bfree*stat.f_bsize
    print("Available space: " + str(freeSpace))
    while(freeSpace < minFreeSpace):
        oldestMissionNumber = currentMissionNumber
        for folder in os.listdir(baseFolder):
            number = 0
            try:
                if(int(folder) < oldestMissionNumber):
                    oldestMissionNumber = int(folder)
            except ValueError:
                continue
        if(oldestMissionNumber != currentMissionNumber):
            print("Remove " + baseFolder+ "/" + str(oldestMissionNumber))
            shutil.rmtree(baseFolder + "/" + str(oldestMissionNumber))

path, baseFolder, missionNumber = setupFolders();
print("Writing to " + path)
i = 0;
drone = BwDrone.BwDrone()
drone.connect()
while(True):
    print("Take picture " + str(i))
    image = getPicture(path, i);
    position = drone.getPosition()
    addExifData(image, position)
    checkDiskSpaceAndClean(baseFolder, missionNumber)
    sleep(3);
    i = i + 1;

