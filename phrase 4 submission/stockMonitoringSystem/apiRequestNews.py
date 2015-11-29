import requests
import xml.etree.ElementTree as ET
from codecs import EncodedFile

mUrl = "http://rss.cnn.com/rss/money_news_international.rss";
title = []
link = []

class apiRequestNews():
	def __init__(self, parent):
		resp = requests.get(mUrl, stream=True)
		if 200 != resp.status_code:
			return False

		self.root = ET.fromstring(resp.content)
		self.channel = self.root.find('channel')
		for elem in self.channel.findall('item'):
			title.append(elem.find('title').text)
			link.append(elem.find('link').text)
			# print self.title.text, self.link.text
		# self.item = self.channel.find('item')
		# self.title = self.item.find('title')
		# self.link = self.item.find('link')
	def GetTitleList(self,event):
		return title

	def GetLinkList(self,event):
		return link
