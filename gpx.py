import sys
import xml.dom.minidom

from handlers import GPXHandler
from xml.sax import make_parser

L = []
ch = GPXHandler('2016-10-23T07:39:41.000Z', '2016-10-23T07:40:34.000Z', L)
saxparser = make_parser()

saxparser.setContentHandler(ch)
saxparser.parse("t1.xml")

#print(ch.getContent())

xml = xml.dom.minidom.parseString(ch.getContent())
pretty_xml_as_string = xml.toprettyxml(indent='  ')

print(pretty_xml_as_string)

