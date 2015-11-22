import urllib2

class downloadFile:
    def __init__(self,url, extendURL, saveName):
        self.url = url
        self.extendURL = extendURL
        self.saveName = saveName
        
    def download(self):
        fullURL = self.url+self.extendURL
        loadFile = urllib2.urlopen(fullURL)
        path = self.saveName
        output = open(path,'wb')
        output.write(loadFile.read())
        output.close()
    
    
#dl = downloadFile('http://cn.wsj.com/big5/rssHKstock.xml', 'news.xml')
#dl.download()

dl = downloadFile('http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=', '00001', '00001.xml')
dl.download()
