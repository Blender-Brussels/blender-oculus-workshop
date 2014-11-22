

from pyOSC import OSCServer
import sys
import bge
from bge import logic
from time import sleep
from mathutils import *

server = OSCServer( ("localhost", 7120) )
server.timeout = 0
run = True

mycont=logic.getCurrentController()
joueur=mycont.owner
eu = Euler((0, 0, 0), 'XYZ')

# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False
def handle_timeout(self):
    self.timed_out = True

# funny python's way to add a method to an instance of a class
import types
server.handle_timeout = types.MethodType(handle_timeout, server)

def user_callback(path, tags, args, source):
    # which user will be determined by path:
    # we just throw away all slashes and join together what's left
    user = ''.join(path.split("/"))
    # tags will contain 'fff'
    # args is a OSCMessage with data
    # source is where the message came from (in case you need to reply)
    #print ("Now do something with", user, args[0], args[1], args[2], args[3]) 
    bge.logic.rotation = Quaternion((   -args[1], args[2], args[0], args[3] ))
    
    # OpenHMD send quaternion data in the format Y-WXZ, blender needs WXYZ
    # angle seesm inverted too... 
#    try:
#        eu = bge.logic.rotation.to_euler()
#    except AttributeError:
#        eu = Euler((0, 0, 0), 'XYZ')
    #rot = Euler((-eu.z, eu.y, -eu.x), 'XYZ')
#    rot = Euler((-eu.z, eu.y, -eu.x), 'XYZ')
#    fix = Euler((0, 0, 0), 'XYZ')
    #fix = Euler((-1.5707963705062866, 0, 0), 'XYZ')
#    rot.rotate(fix)
    joueur.localOrientation = bge.logic.rotation
    

#def quit_callback(path, tags, args, source):
#    # don't do this at home (or it'll quit blender)
#    global run
#    run = False
#    server.close()

server.addMsgHandler( "/user/1", user_callback )

#server.addMsgHandler( "/quit", quit_callback )

# user script that's called by the game engine every frame
def each_frame():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()


# simulate a "game engine"

def quit():
    server.close()

