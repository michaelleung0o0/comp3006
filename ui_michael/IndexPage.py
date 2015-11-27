import wx
import wx.xrc
import wx.richtext
import sys

from Login import Login
from Welcome import Welcome
from Register import Register
from Forget_password import Forget_password
from Monitoring_stock import Monitoring_stock
from Search_Stock import Search_Stock
from Setting import Setting
from Finances import Finances
from Admin import Admin
from About_Us import About_Us

num = 0;
Finances_L = None
login = None
welcome = None
search = None
monitoring = None
finances = None
admin = None

class IndexPage ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,620 ))
		
		self.SetMinSize( wx.Size( 900,570 ) )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.w_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Exit = wx.Button( self.w_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.Exit, 0, wx.ALL, 5 )
		
		self.Logout = wx.Button( self.w_panel, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.Logout, 0, wx.ALL, 5 )
		
		self.Home = wx.Button( self.w_panel, wx.ID_ANY, u"&Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.Home, 0, wx.ALL, 5 )
		
		self.News = wx.Button( self.w_panel, wx.ID_ANY, u"&News", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.News, 0, wx.ALL, 5 )
		
		self.Search_stock = wx.Button( self.w_panel, wx.ID_ANY, u"Search stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.Search_stock, 0, wx.ALL, 5 )
		
		self.Monitoring_Stock = wx.Button( self.w_panel, wx.ID_ANY, u"Monitoring Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.Monitoring_Stock, 0, wx.ALL, 5 )
		
		self.Setting = wx.Button( self.w_panel, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.Setting, 0, wx.ALL, 5 )
		
		self.About_Us = wx.Button( self.w_panel, wx.ID_ANY, u"About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.About_Us, 0, wx.ALL, 5 )
		
		self.Admin = wx.Button( self.w_panel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.Admin, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.w_panel.SetSizer( bSizer1 )
		self.w_panel.Layout()
		bSizer1.Fit( self.w_panel )
		bSizerFrame.Add( self.w_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizerFrame )
		self.Layout()
		
		# Connect Events
		self.Exit.Bind( wx.EVT_BUTTON, self.ExitOnButtonClick )
		self.Logout.Bind( wx.EVT_BUTTON, self.onLogout )
		self.Home.Bind( wx.EVT_BUTTON, self.onHome )
		self.News.Bind( wx.EVT_BUTTON, self.onNews )
		self.Search_stock.Bind( wx.EVT_BUTTON, self.onSearch )
		self.Monitoring_Stock.Bind( wx.EVT_BUTTON, self.onMonitoring )
		self.Setting.Bind( wx.EVT_BUTTON, self.onSetting )
		self.About_Us.Bind( wx.EVT_BUTTON, self.onAbout )
		self.Admin.Bind( wx.EVT_BUTTON, self.onAdmin )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	
	
	def ExitOnButtonClick( self, event ):
		sys.exit(0)
	
	def onLogout( self, event ):
		self.Hide()
		Login.Show()






	def onNews(  self ,event ):
		self.destroyall( self )
		global finances
		finances = Finances(self)
		finances.Show()
		global num
		num = 1

	def onSearch(  self ,event ):
		self.destroyall( self )
		global search
		search = Search_Stock( self )
		search.Show()
		global num
		num = 2

	def onMonitoring(  self ,event ):
		self.destroyall( self )
		global monitoring
		monitoring = Monitoring_stock(self)
		monitoring.Show()
		global num
		num = 3

	def onSetting(  self ,event ):
		#self.destroyall( self )
		self.Setting = Setting(self)
		self.Setting.Show()
	
	def onAbout(  self ,event ):
		#self.destroyall( self )
		self.About_Us = About_Us(self)
		self.About_Us.Show()
	
	def onAdmin( self ,event):
		self.destroyall( self )
		global admin
		admin = Admin( self )
		admin.Show()
		global num
		num = 4

	def onHome(  self ,event ):
		self.destroyall( self )
		global welcome
		welcome = Welcome( self )
		welcome.Show()
		global num
		num = 5

	def destroyall( self , event):
		global num
		if num ==1:
			global finances
			finances.Destroy()
			finances = None
		if num ==2:
			global search
			search.Destroy()
			search = None
		if num ==3:
			global monitoring
			monitoring.Destroy()
			monitoring = None
		if num ==4:
			global admin
			admin.Destroy()
			admin = None
		if num ==5:
			global welcome
			welcome.Destroy()
			welcome = None
		num = 0
		self.w_panel.Update()
		