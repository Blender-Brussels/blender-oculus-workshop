

from rift import PyRift
from pyOSC import OSCClient, OSCMessage

rotrift = PyRift()

def initialisation():
    client = OSCClient()
    client.connect( ("127.0.0.1", 7120) )

def send():
    client = OSCClient()
    message = OSCMessage()
    message.setAddress("/user/1")
    message.append([rotrift.rotation[0], 
    rotrift.rotation[1], 
    rotrift.rotation[2], 
    rotrift.rotation[3]])
    #client.send( message, message.append([arg1, arg2, arg3])    
    #client.send( message)
    try:
        client.sendto(message, ('127.0.0.1', 7120))
        message.clearData()
    except:
        print('connection refused')



while True:
  rotrift.poll()
  print("rotation quat: %f %f %f %f" % (rotrift.rotation[0], rotrift.rotation[1], rotrift.rotation[2], rotrift.rotation[3]))
  send()



