#from urllib2 import Request, urlopen, URLError
#from downloadFile import downloadFile
import requests
import xml.etree.ElementTree as ET




class xmlReader:
    def __init__(self, url, extendURL):
        self.url = url
        self.extendURL = extendURL
        self.mUrl = url+extendURL
        
    def requestXML(self):
        resp = requests.get(self.mUrl, stream=True)
        if 200 != resp.status_code:
            return False
        return resp.content
    def requestStockXML(self):
        xml = self.requestXML().replace("utf8", "utf-8")
        root = ET.fromstring(xml)
        return root
        #print root.tag
        #stock = root.find('stock')
        #server = stock.find('server')
        #name = stock.find('name')
        #chinese = name.find('chinese')
        #schinese = name.find('schinese')
        #english = name.find('english')
        #price = stock.find('price')
        #print english.text , price.text
    def requestNewsXML(self):
        xml = self.requestXML().decode('big5').encode('utf-8')
        root = ET.fromstring(xml)
        return root

        
xr = xmlReader("http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=", "00001")
print xr.requestStockXML().find('stock').find('name').find('chinese').text
xr2 = xmlReader("http://cn.wsj.com/big5/rssHKstock.xml", "")
print xr2.requestNewsXML().find('item').decode('big5')
