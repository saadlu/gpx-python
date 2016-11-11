from xml.sax.handler import ContentHandler
from datetime import datetime

#t = datetime.datetime.strptime("2016-10-23T07:39:42.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")

class GPXHandler(ContentHandler):

    def __init__(self, fromDate, toDate, container):
        self.inTrk = False
        self.inTrkSeg = False
        self.inTrkPt = False
        self.inTime = False
        self.addTrkPt = False
        
        self.timeText = ''
        self.trkPtText = ''

        self.fromDate = datetime.strptime(fromDate, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.toDate = datetime.strptime(toDate, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.container = container

        self.content = ''

    def getContent(self):
        return self.content
    
    def startElement(self, name, attrs):
        if name == 'trkpt':
            self.inTrkPt = True
        elif self.inTrk and name == 'time':
            self.timeText = ''
            self.inTime = True
        elif name == 'trk':
            self.inTrk = True 

        if self.inTrkPt:     
            self.trkPtText += '<' + name
            for item in attrs.items():
                self.trkPtText += ' ' + item[0] + '="' + item[1] + '"'
            self.trkPtText += '>'
        else:
            self.content += '<' + name
            for item in attrs.items():
                self.content += ' ' + item[0] + '="' + item[1] + '"'
            self.content += '>'
            
    def characters(self, characters):

        if self.inTrkPt:
            self.trkPtText += characters.strip()
        else:
            self.content += characters.strip()
            
        if self.inTime:
            self.timeText += characters
            
    def endElement(self, name):
        if self.inTrkPt:
            self.trkPtText += '</' + name + '>'
      
        else:
            self.content += '</' + name + '>'
            
        if self.inTime and name == 'time':
            self.inTime = False
            ftime = datetime.strptime(self.timeText, "%Y-%m-%dT%H:%M:%S.%fZ")
            if self.fromDate >= ftime:
                self.addTrkPt = True
            else:
                self.addTrkPt = False
        elif name == 'trk':
            self.inTrk = False
        elif name == 'trkpt':
            self.inTrkPt = False
            if self.addTrkPt:
                self.content += self.trkPtText
            #print(self.trkPtText)
            self.trkPtText = ''
                
        
