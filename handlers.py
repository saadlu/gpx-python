from xml.sax.handler import ContentHandler
from datetime import datetime

#t = datetime.datetime.strptime("2016-10-23T07:39:42.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")

class GPXHandler(ContentHandler):

    def __init__(self, fromDate, toDate, container):
        self.inTrkSeg = False
        self.inTrkPt = False
        self.inTime = False
        self.timeValue = ''
        self.trkPtText = ''

        self.fromDate = datetime.strptime(fromDate, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.toDate = datetime.strptime(toDate, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.container = container

        self.content = ''

    def getContent(self):
        return self.content
    
    def startElement(self, name, attrs):
        self.content += '<' + name

        for item in attrs.items():
            self.content += ' ' + item[0] + '="' + item[1] + '"'

        self.content += '>'
        # if name == 'trkseg':
        #     self.inTrkSeg = True
            
        # elif self.inTrkSeg and name == 'trkpt':
        #     self.inTrkPt = True
        #     self.trkPtText = ''

        # elif self.inTrkPt:
        #     self.trkPtText += '<' + name + '>'
            
        #     if name == 'time':
        #         self.inTime = True
        #         self.timeValue = ''
            

    def characters(self, characters):
        self.content += characters.strip()
        
        if self.inTime:
            self.timeValue += characters

        if self.inTrkPt:
            self.trkPtText += characters
            
    def endElement(self, name):
        # if name == 'time':
        #     self.inTime = False
        #     ftime = datetime.strptime(self.timeValue, "%Y-%m-%dT%H:%M:%S.%fZ")
        #     if ftime >= self.fromDate and ftime <= self.toDate:
        #         self.container.append(self.trkPtText)
            
        # elif name == 'trkpt':
        #     self.inTrkPt = False
        #     self.trkPtText += '</trkpt>'
            
        #     if name == 'time':
        #         self.inTime = False
        #         ftime = datetime.strptime(self.timeValue, "%Y-%m-%dT%H:%M:%S.%fZ")
                
        self.content += '</' + name + '>'
                    