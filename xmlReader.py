from urllib2 import Request, urlopen, URLError

class xmlReader:
    def __init__(self, url):
        
        self.url = url
        
    def showURL(self):
        print self.url
        
    def requestXML(self):
        #print "XML request"
        #print "url = " + self.url
        
        try:
            request = Request(self.url)
            response = urlopen(request)
            xmlContent = response.read()
            #print xmlContent
            #print "requestXML -------------------------"
            return xmlContent
    
        except URLError, e:
            print 'Got an error code:', e

    def decodeBig5(self, input):
        return input.decode('big5')
    
    def encodeUTF8(self, input):
        return input.encode('utf-8')

