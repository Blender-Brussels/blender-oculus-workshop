from game_engine_rift.rift import PyRift
from mathutils import *

# bge.logic.rift = PyRift()
 
def poll(rift):
    rift.poll()
    bge.logic.rotation = Quaternion((rift.rotation[0],
        rift.rotation[1],
        rift.rotation[2],
        rift.rotation[3]))
 

# 
#
try:
    poll(bge.logic.rift)
except AttributeError:
    bge.logic.rift = PyRift()
#    
print(bge.logic.rift.rotation[0])

try:
    eu = bge.logic.rotation.to_euler()
except AttributeError:
    eu = Euler((0, 0, 0), 'XYZ')

print(eu) 
# 
scene = bge.logic.getCurrentScene()
#cam = scene.active_camera
cont = bge.logic.getCurrentController()
fix = Euler((-1.5707963705062866, 0, 0), 'XYZ')
obj = cont.owner
rot = Euler((-eu.z, eu.y, -eu.x), 'XYZ')
rot.rotate(fix)
obj.localOrientation = rot
#cam.worldOrientation = rot