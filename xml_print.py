#!/usr/bin/env python
"""Python example.

XML processing
"""

import sys, os, argparse
try:
    from xml.etree.cElementTree  import ElementTree # fast
except ImportError:
    from xml.etree.ElementTree  import ElementTree


def print_xml_file(xml_file):
    #create an ElementTree instance from an XML file
    doc = ElementTree(file=xml_file)
    #write out XML from the ElementTree instance
    doc.write(sys.stdout, xml_declaration=True, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process .xml file')
    parser.add_argument('xml_file', help='The .xml file to process')
    args = parser.parse_args()
    print_xml_file(args.xml_file)

