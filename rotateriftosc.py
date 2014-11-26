

from pyOSC import OSCServer
import sys
import bge
from bge import logic
from time import sleep
from mathutils import *

# need a global reference for the callback
# it is initialized in the init
joueur=None


# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False
def handle_timeout(self):
    self.timed_out = True

# funny python's way to add a method to an instance of a class
import types


def user_callback(path, tags, args, source):

    # OpenHMD send quaternion data in the format Y-WXZ, blender needs WXYZ
    # angle seesm inverted too... 

    #print ("Now do something with", user, args[0], args[1], args[2], args[3]) 
    joueur.localOrientation = Quaternion(( -args[1], args[2], args[0], args[3] ))
    



def init(cont):
    global joueur
    joueur = cont.owner
    server = OSCServer(("localhost", 7120))
    server.timeout = 0
    server.handle_timeout = types.MethodType(handle_timeout, server)
    server.addMsgHandler( "/user/1", user_callback )
    # keep a reference in the object dictionary: it will be automatically deleted on game exit
    joueur.attrDict["server"] = server
    
    
# user script that's called by the game engine every frame
def each_frame(cont):
    # clear timed_out flag
    server = cont.owner.attrDict["server"]
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()

