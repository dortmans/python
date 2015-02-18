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

XML processing
--------------
References

- [Processing XML in Python with ElementTree](http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree)
- [Python 101 – Intro to XML Parsing with ElementTree](http://www.blog.pythonlibrary.org/2013/04/30/python-101-intro-to-xml-parsing-with-elementtree/)
- [ElementTree Overview](http://effbot.org/zone/element-index.htm)
- [The ElementTree XML API](https://docs.python.org/2/library/xml.etree.elementtree.html)
- [The lxml.etree Tutorial](http://lxml.de/tutorial.html)

### XMI
References:

- [Working XML: UML, XMI, and code generation](http://gusconstan.com/webservices/xmi/index.htm)
- [OMG Model Interchange Test Suite](http://www.omgwiki.org/model-interchange/doku.php?id=start#test_suite)
- [The UML DTD and what is needed](http://www.gupro.de/mirror/xig/xmi.the_uml_dtd/xmi_the_uml_dtd.htm)
- [xmi2code project](https://github.com/charlycoste/xmi2code)
- [PlantUML](http://plantuml.sourceforge.net/xmi.html)

