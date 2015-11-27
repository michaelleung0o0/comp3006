import requests
import xml.etree.ElementTree as ET
from codecs import EncodedFile

mUrl = "http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=00001";
# mUrl = 'http://cn.wsj.com/big5/rssHKstock.xml'
# from_encoding = 'big5'
# to_encoding = 'utf-8'
price = None
chinese = None

class apiRequest():
   def __init__(self, parent):
		# super(apiRequest, self).__init__()
      # english = None
		# self.GetStockRequest()

  #  def GetStockRequest(self):
      resp = requests.get(mUrl, stream=True)
      if 200 != resp.status_code:
         return False
	        # xml = resp.content.replace("big5","utf-8")
	        # xml = resp.content.decode('big5')
	        # data = xml.decode('utf-8')
            # root = ET.fromstring(data)
      xml = resp.content.replace("utf8","utf-8")
      root = ET.fromstring(xml)
      print root.tag
      stock = root.find('stock')
      server = stock.find('server')
      name = stock.find('name')
      chinese = name.find('chinese')
      schinese = name.find('schinese')
      self.english = name.find('english').text
      price = stock.find('price')
      # print self.english , price.text

   # def GetChineseName(self):
   #    return chinese.text

   # def GetPrice(self):
   #    return price.text

   def GetEnglishName(self):
      return self.english