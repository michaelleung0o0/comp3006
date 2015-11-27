from urllib2 import Request, urlopen, URLError
from downloadFile import downloadFile



class xmlReader:
    def __init__(self, url, extendURL, XMLName):
        self.dlFile = downloadFile(url, extendURL, XMLName)
        self.url = url
        self.extendURL = extendURL
        self.XMLName = XMLName
        
        
    def showFullURL(self):
        #print self.url + self.extendURL
        return self.url + self.extendURL
        
    def requestXML(self):
        #print "XML request"
        #print "url = " + self.url
        self.dlFile.download()
        
        with open (self.XMLName, "r") as myfile:
            data=myfile.read()
        return data

    def decodeBig5(self, input):
        return input.decode('big5')
    
    def encodeUTF8(self, input):
        return input.encode('utf-8')


#xr = xmlReader('http://cn.wsj.com/big5/rssHKstock.xml', '', 'news.xml')
#xr1 = xmlReader('http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=', '00001', '00001.xml')
#xr.showFullURL()
#xr1.showFullURL()
#print xr1.requestXML()
