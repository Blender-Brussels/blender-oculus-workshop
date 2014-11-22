blender-oculus-workshop
=======================

Files for the Blender + Oculus workshop @ iMAL

Notes
-----

http://piratepad.be/p/blender-oculus
   
References 
based on work at http://lubosz.wordpress.com/2013/06/26/oculus-rift-support-in-blender-game-engine/
https://github.com/OpenHMD/OpenHMD
https://developer.oculus.com/downloads/
installation on linux (opensource solution):
on xubuntu 12.04, step by step
install OpenHMD from github >> https://github.com/OpenHMD/OpenHMD
hidapi is not available via apt-get, compile it from source > its a subdirectory in the github tree
once done, go to folder "examples/"
// 1.
run "make"
connect the oculus rift (VK2 tested)
go to "examples/simple/"
in terminal and launch "./simple"
you should see the quaternion printing
// 2
opengl example requires a bit more of works...
$ sudo apt-get install libsdl-dev
go to gl.h and adapt include #include <SDL.h> to #include <SDL/SDL.h>
[waiting for benoit to debug the rest...]
https://github.com/lubosz/python-rift
/!\ change path for include openhmd in setup.py : 
usr/local/include inplace of usr/include
dependancy : cython3
apt-get install Cython3
compile with python3 : 
$ python3 setup.py build
$ su
# python3 setup.py install
# ldconfig
# exit
for python > OSC
add pyOSC.py to directory
https://github.com/Blender-Brussels/blender-oculus-workshop/blob/master/pyOSC.py
and launch 
$ python3 riftosc.py
https://github.com/Blender-Brussels/blender-oculus-workshop/blob/master/riftosc.py
Install drivers (Linux Mint 17) :
- autotools
- automake
- libhidapi-dev libhidapi-lsusb0
- libtool
- OpenHMD (! DO NOT DOWNLOAd ZIP - GIT CLONE ONLY ) merci :)
- cf git (udev rules, run examples)
- and tadaam..
Blender files for running games with the Oculus stack:
https://github.com/Blender-Brussels/blender-oculus-workshop
interested in vision/oculomotor neuroscience, cooperation for experimental design, and/or a lab visit, please feel free write me an e-mail to:
kim.wende@uclouvain.be
For mac users:
Download Oculus Runtime for Mac OSX and Oculus SDK for Mac OSX https://developer.oculus.com/downloads/
Launch the .dmg from Oculus Runtime, then launch the Oculus Runtime application, let it install. Then, open the Oculus SDK archive, before plugging in the Oculus. Try out by launching OculusWorldDemo in the Oculus SDK folder.

