from xmlReader import xmlReader
url = 'http://cn.wsj.com/big5/rssHKstock.xml'


class readNews():
    #xmlReader = None
    
    def __init__(self, url):
        self.xmlread = xmlReader(url,'')
        self.xmlstring = self.xmlread.requestNewsXML()
    
    #def itemList(self):
        #allItems = self.xmlstring.findall('item')
        #print allItems



    #def getTitle(self):
        
        #titleList = allItems.findall('title')
        #return titleList

rn = readNews(url)
rn.itemList()
