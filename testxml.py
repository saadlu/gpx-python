import xml.dom.minidom

doc = xml.dom.minidom.parse("d1.gpx")

first = doc.getElementsByTagName("trkpt")[0];

firstTime = first.getElementsByTagName("time")[0].firstChild.nodeValue

dateutil.parser.parse("test.xml")
