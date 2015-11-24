import wx
import os
import requests
# from urllib2 import Request, urlopen, URLError
# from xml.etree import ElementTree
# from cStringIO import StringIO
import xml.etree.ElementTree as ET
import urllib2
# from lxml import etree

mAppName = "Stock Management System";
mAppWidth = 800;
mAppHeight = 600;
mUrl = "http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=00001";

class windowClass(wx.Frame):
	"""
	Stock Managment System
	"""
	def __init__(self, *arg, **kwargs):
		super(windowClass, self).__init__(*arg, **kwargs)

		self.basicGUI()

	def basicGUI(self):
		# panel
		panel = wx.Panel(self)

		# menu
		menuBar = wx.MenuBar()
		fileButton = wx.Menu()
		editButton = wx.Menu()
		exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status msg...')

		menuBar.Append(fileButton, 'File')
		menuBar.Append(editButton, 'Edit')

		self.SetMenuBar(menuBar)

		# wx.TextCtrl(panel, pos=(100, 100), size=(20, 20))
		dataText = wx.StaticText(panel, -1, 'test', (3,3) )

		callbtn = wx.Button(panel, -1, "CallRequest", (50, 0))

		self.Bind(wx.EVT_BUTTON, self.GetStockRequest, callbtn)
		self.Bind(wx.EVT_MENU, self.Quit, exitItem)

		self.SetTitle(mAppName)

		self.Show(True)


	def GetStockRequest(self,evt):
        	# request = Request(mUrl)

	        # try:
	            # response = urlopen(request)
	            # resp = response.read()

	            resp = requests.get(mUrl, stream=True)
	            if 200 != resp.status_code:
	            	return False

	            # print resp.status_code
	            # print resp.headers['content-type']
	            # print resp.encoding

	            xml = resp.content.replace("utf8", "utf-8")
	            root = ET.fromstring(xml)
	            print root.tag
	            stock = root.find('stock')
	            #
	            server = stock.find('server')
				#
	            name = stock.find('name')
	            chinese = name.find('chinese')
	            schinese = name.find('schinese')
	            english = name.find('english')
	            #
	            price = stock.find('price')
	            print english.text , price.text

	            # os.system('python CallRequest.py')

	def Quit(self,e):
		self.Close()

def main():
	app = wx.App()
	windowClass(None)
	app.MainLoop()

main()