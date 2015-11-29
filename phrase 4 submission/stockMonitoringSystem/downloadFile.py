# import urllib2
from urllib2 import Request, urlopen, URLError

class downloadFile:
    def __init__(self,url, saveName):
        print 'init dl'
        self.url = url
        # self.extendURL = extendURL
        self.saveName = saveName

    def download(self):
        # fullURL = self.url
        # + self.extendURL
        print 'url = ' + self.url
        loadFile = urlopen(self.url)
        path = self.saveName
        output = open(path,'wb')
        output.write(loadFile.read())
        output.close()


#dl = downloadFile('http://cn.wsj.com/big5/rssHKstock.xml', 'news.xml')
#dl.download()

# dl = downloadFile('http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=', '00001', '00001.xml')
# dl.download()
