import requests
import xml.etree.ElementTree as ET
from codecs import EncodedFile

mUrl = "http://rss.cnn.com/rss/money_news_international.rss";

class apiRequestNews():
	def __init__(self, parent):
		resp = requests.get(mUrl, stream=True)
		if 200 != resp.status_code:
			return False

		self.root = ET.fromstring(resp.content)
		self.channel = self.root.find('channel')
		for data in self.channel:
			for item in data:
				print item.text
			# self.title = item.find('title')
			# self.link = item.find('link')
			# print self.title
		# for data in self.item:
		# 	self.title = data.find('title')
		# 	self.link = data.find('link')
		# 	print self.title
		# 	print self.link

		# print self.item.tag
		# print self.item.attrib

		# for content in self.channel:
  #   			self.title = content.find('title').attrib
  #   			# self.link = content.tag.find('link').text
  #   			print self.title.text
  #   			# print content.tag
  #   			# print content.attrib

   # def GetChineseName(self, event):
   #    return self.chinese

   # def GetSchineseName(self, event):
   #    return self.schinese

   # def GetEnglishName(self, event):
   #    return self.english

   # def GetCurrentPrice(self, event):
   #    return self.price

   # def GetPrefixPrice(self, event):
   #    return self.pexit

   # def GetHighPrice(self, event):
   #    return self.highPrice

   # def GetLowPrice(self, event):
   #    return self.lowPrice

   # def GetChange(self, event):
   #    return self.change

   # def GetPctChange(self, event):
   #    return self.pctChange

   # def UpdateSearchCode(self,event, symbol):
   #    mUrl = 'http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=' + symbol
   #    print mUrl
