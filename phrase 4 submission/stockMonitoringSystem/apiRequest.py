import requests
import xml.etree.ElementTree as ET
from codecs import EncodedFile

mUrl = "http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=";
# mUrl = 'http://cn.wsj.com/big5/rssHKstock.xml'
# from_encoding = 'big5'
# to_encoding = 'utf-8'


class apiRequest():
   def __init__(self, parent, symbol):
		# super(apiRequest, self).__init__()
      # english = None
		# self.GetStockRequest()

  #  def GetStockRequest(self):
      url = mUrl + symbol
      resp = requests.get(url, stream=True)
      if 200 != resp.status_code:
         return False
	        # xml = resp.content.replace("big5","utf-8")
	        # xml = resp.content.decode('big5')
	        # data = xml.decode('utf-8')
            # root = ET.fromstring(data)
      xml = resp.content.replace("utf8","utf-8")
      self.root = ET.fromstring(xml)
      # print root.tag
      self.stock = self.root.find('stock')
      self.server = self.stock.find('server')
      self.name = self.stock.find('name')
      # self.chinese = self.name.find('chinese').text
      #self.schinese = self.name.find('schinese').text
      self.english = self.name.find('english').text
      self.price = self.stock.find('price').text
      self.pexit = self.stock.find('pexit').text
      self.highPrice = self.stock.find('high').text
      self.lowPrice = self.stock.find('low').text
      self.change = self.stock.find('change').text
      self.pctChange = self.stock.find('pct_change').text

   # def GetChineseName(self, event):
   #    return self.chinese

   # def GetSchineseName(self, event):
   #    return self.schinese

   def GetEnglishName(self, event):
      return self.english

   def GetCurrentPrice(self, event):
      return self.price

   def GetPrefixPrice(self, event):
      return self.pexit

   def GetHighPrice(self, event):
      return self.highPrice

   def GetLowPrice(self, event):
      return self.lowPrice

   def GetChange(self, event):
      return self.change

   def GetPctChange(self, event):
      return self.pctChange

   def UpdateSearchCode(self,event, symbol):
      mUrl = 'http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=' + symbol
      print mUrl
