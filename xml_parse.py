# Source: http://www.blog.pythonlibrary.org/2013/04/30/python-101-intro-to-xml-parsing-with-elementtree/
# http://lxml.de/tutorial.html

try:
    from lxml import etree as ET

    print("running with lxml.etree")
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as ET

        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as ET

            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as ET

                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as ET

                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")

#----------------------------------------------------------------------
def parseXML(xml_file):
    """
    Parse XML with ElementTree
    """
    tree = ET.ElementTree(file=xml_file)
    print tree.getroot()
    root = tree.getroot()
    print "tag=%s, attrib=%s" % (root.tag, root.attrib)

    for child in root:
        print child.tag, child.attrib
        if child.tag == "appointment":
            for step_child in child:
                print step_child.tag

    # iterate over the entire tree
    print "-" * 40
    print "Iterating using a tree iterator"
    print "-" * 40
    # iter_ = tree.getiterator() DEPRECATED
    iter_ = tree.iter()
    for elem in iter_:
        print elem.tag

    # get the information via the children!
    print "-" * 40
    print "Iterating using getchildren()"
    print "-" * 40
    appointments = root.getchildren()
    for appointment in appointments:
        appt_children = appointment.getchildren()
        for appt_child in appt_children:
            print "%s=%s" % (appt_child.tag, appt_child.text)

#----------------------------------------------------------------------
if __name__ == "__main__":
    parseXML("./data/appt.xml")