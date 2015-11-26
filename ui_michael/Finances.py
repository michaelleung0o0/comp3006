import wx
import wx.xrc
import wx.richtext
import sys

from readNews import readNews
# from apiRequest import apiRequest
###########################################################################
## Class Finances
###########################################################################

class Finances ( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.TAB_TRAVERSAL )

		self.SetMinSize( wx.Size( 900,600 ) )

		bSizerFrame = wx.BoxSizer( wx.VERTICAL )

		self.f_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self.f_panel, wx.ID_ANY, u"Finances News", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )

		bSizer2.Add( self.title, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer3.SetMinSize( wx.Size( -1,400 ) )
		self.main_c = wx.richtext.RichTextCtrl( self.f_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer3.Add( self.main_c, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.Exit = wx.Button( self.f_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Exit, 0, wx.ALL, 5 )

		self.Logout = wx.Button( self.f_panel, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Logout, 0, wx.ALL, 5 )

		self.Home = wx.Button( self.f_panel, wx.ID_ANY, u"&Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Home, 0, wx.ALL, 5 )

		self.News = wx.Button( self.f_panel, wx.ID_ANY, u"&News", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.News, 0, wx.ALL, 5 )

		self.Search_stock = wx.Button( self.f_panel, wx.ID_ANY, u"Search stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Search_stock, 0, wx.ALL, 5 )

		self.Monitoring_Stock = wx.Button( self.f_panel, wx.ID_ANY, u"Monitoring Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Monitoring_Stock, 0, wx.ALL, 5 )

		self.Setting = wx.Button( self.f_panel, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Setting, 0, wx.ALL, 5 )

		self.About_Us = wx.Button( self.f_panel, wx.ID_ANY, u"About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.About_Us, 0, wx.ALL, 5 )

		self.Admin = wx.Button( self.f_panel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Admin, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 0, 0, 5 )


		self.f_panel.SetSizer( bSizer1 )
		self.f_panel.Layout()
		bSizer1.Fit( self.f_panel )
		bSizerFrame.Add( self.f_panel, 1, wx.EXPAND |wx.ALL, 5 )


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

		self.readNews = readNews(self)
		self.readNews.RSSReader()
		# self.apiRequest = apiRequest(self)
	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ExitOnButtonClick( self, event ):
		event.Skip()

	def onLogout( self, event ):
		event.Skip()

	def onHome( self, event ):
		event.Skip()

	def onNews( self, event ):
		event.Skip()

	def onSearch( self, event ):
		event.Skip()

	def onMonitoring( self, event ):
		event.Skip()

	def onSetting( self, event ):
		event.Skip()

	def onAbout( self, event ):
		event.Skip()

	def onAdmin( self, event ):
		event.Skip()
