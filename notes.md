Python notes
============

PIP
---
Install PIP:
    
    sudo apt-get install python-pip
    
    
LiClipse
--------
This advanced Eclipse distribution includes [PyDev](http://pydev.org/)
Alternative IDE: [PyCharm](https://www.jetbrains.com/pycharm/)

Unpack and install:

    tar xfz liclipse_VERSION_linux.gtk.ARCH.tar.gz (replacing VERSION and ARCH properly) 
    sudo ln -s `pwd`/liclipse/LiClipse /usr/bin/liclipse
 
Start it:

    liclipse
 
 Set path to Python interpreter. You can find it easy like this:
 
    which python
 

PyCharm
-------
Download Community edition [here](https://www.jetbrains.com/pycharm/download/).

Unpack:

    tar xvf pycharm-community-4.0.4.tar.gz

Check if java is installed:

    java -version

If it says "The program 'java' can be found in ..." install it:

    sudo apt-get install default-jre

Start PyCharm:
    
    ~/pycharm-community-*/bin/pycharm

Lock to launcher if you want.



