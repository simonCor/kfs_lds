import picamera
import os
import shelve
from time import sleep
from os.path import expanduser

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
    camera.capture(folder + "/" + str(i) + '.jpg')
    sleep(3)

path = setupFolders();
i = 0;
while(True):
    print("Take picture " + str(i))
    getPicture(path, i);
    sleep(3);
    i = i + 1;

