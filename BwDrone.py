import sys, os

dronekitPath = os.getcwd() + '/dronekit-python'
print "Import path: " + dronekitPath
sys.path.append(dronekitPath)
from dronekit import connect, VehicleMode

class BwDrone:
    connection_string = "/dev/ttyAMA0"
    vehicle = ""

    def connect(self):
        print("Connecting to vehicle on: %s" % (self.connection_string,))
        self.vehicle = connect(self.connection_string, baud=57600, wait_ready=True, heartbeat_timeout=30)

    def getPosition(self):
        return self.vehicle.location.global_frame

    def close(self):
        self.vehicle.close()
