import requests
import xml.etree.ElementTree as ET
from codecs import EncodedFile

# mUrl = "http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=00001";
mUrl = 'http://cn.wsj.com/big5/rssHKstock.xml'
from_encoding = 'big5'
to_encoding = 'utf-8'

class apiRequest():
	def __init__(self, parent):
		# super(apiRequest, self).__init__()
		self.GetStockRequest()

	def GetStockRequest(self):
	    resp = requests.get(mUrl, stream=True)
	    if 200 != resp.status_code:
	        return False
	        # xml = resp.content.replace("big5","utf-8")
	        # xml = resp.content.decode('big5')
	        # data = xml.decode('utf-8')
            # root = ET.fromstring(data)

   #          xml = resp.content.replace("utf8", "utf-8")
   #          root = ET.fromstring(xml)
   #          print root.tag
   #          stock = root.find('stock')
   #          #
   #          server = stock.find('server')
			# #
   #          name = stock.find('name')
   #          chinese = name.find('chinese')
   #          schinese = name.find('schinese')
   #          english = name.find('english')
   #          #
   #          price = stock.find('price')
   #          print english.text , price.text
			# xml = resp.content.decode('utf-8')

   #          stock = root.find('stock')
   #          #
   #          server = stock.find('server')
			# #
   #          name = stock.find('name')
   #          chinese = name.find('chinese')
   #          schinese = name.find('schinese')
   #          english = name.find('english')
   #          #
   #          price = stock.find('price')
            # print english.text , price.text
            data = EncodedFile(resp.content, from_encoding, to_encoding)
				print data