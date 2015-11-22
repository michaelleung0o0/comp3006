import wx
import os
import requests
# from urllib2 import Request, urlopen, URLError
# from xml.etree import ElementTree
# import xml.etree.ElementTree as ET
from lxml import etree

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

	            # tree = etree.parse(resp)
	            # print tree.docinfo.doctype

	   #          resp.raw.decode_content = True
	   #          events = ET.iterparse(resp.raw)
				# for elem in events:
				# 	print elem

	            # tree = ET.fromstring(resp.content)
	            # soup = BeautifulSoup(data')
	            # print soup.find('text').string

	            # tree = ET.parse(data)
	            # root = tree.getroot()

	   #          parser = etree.XMLParser(recover=True)
				# etree.fromstring(data, parser=parser)

	            # root = ElementTree.fromstring(data)

	      #       for atype in data.findall('name'):
    			# print(atype.get('chinese'))

	            # msg = resp.content

	            # tree = ET.fromstring(resp)
	            # root = tree.getroot()
	            # for child in tree:
	            	# print child.tag, child.attrib
	            # print(data)
	            # ET.fromstring(resp)

	            # print resp[559:1000]
	            print resp
	            os.system('python CallRequest.py')
	        # except URLError, e:
	        #     print 'No resp. Got an error code:', e

	def Quit(self,e):
		self.Close()

def main():
	app = wx.App()
	windowClass(None)
	app.MainLoop()

main()