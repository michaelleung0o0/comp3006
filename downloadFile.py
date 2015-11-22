import urllib2

class downloadFile:
    def __init__(self,url, saveName):
        self.url = url
        self.saveName = saveName
    def download(self):
        loadFile = urllib2.urlopen(self.url)
        path = '/tmp/' + self.saveName
        output = open(path,'wb')
        output.write(loadFile.read())
        output.close()


dl = downloadFile('http://cn.wsj.com/big5/rssHKstock.xml', 'news.xml')
dl.download()
