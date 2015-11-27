import wx
import wx.xrc
import wx.richtext
import sys
from customString import customString
# Finances_L = None
# Login = None
# Welcome = None
# Search_Stock = None
# Monitoring_stock = None
# finances = None
# Admin = None

###########################################################################
## Class Monitoring_stock
###########################################################################

class Monitoring_stock ( wx.Panel ):

	def __init__( self, parent ):
		self.customString = customString('monitor')
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,570 ), style = wx.TAB_TRAVERSAL )

		self.SetMinSize( wx.Size( 900,600 ) )

		bSizerFrame = wx.BoxSizer( wx.VERTICAL )

		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		try:
			image_file = 'bg.jpg'
			bmp = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			self.bitmap = wx.StaticBitmap(self.m_panel, -1, bmp, (0,0))
		except IOError:
			raise SystemExit

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self.m_panel, wx.ID_ANY, self.customString.title, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )

		bSizer2.Add( self.title, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer3.SetMinSize( wx.Size( -1,400 ) )
		self.main = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RICH|wx.TE_RICH2|wx.TE_WORDWRAP )
		bSizer3.Add( self.main, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.bar = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.bar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.Exit = wx.Button( self.m_panel, wx.ID_ANY, self.customString.exit, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Exit, 0, wx.ALL, 5 )

		self.Logout = wx.Button( self.m_panel, wx.ID_ANY, self.customString.logout, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Logout, 0, wx.ALL, 5 )

		self.Home = wx.Button( self.m_panel, wx.ID_ANY, self.customString.home, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Home, 0, wx.ALL, 5 )

		self.News = wx.Button( self.m_panel, wx.ID_ANY, self.customString.news, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.News, 0, wx.ALL, 5 )

		self.Search_stock = wx.Button( self.m_panel, wx.ID_ANY, self.customString.search, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Search_stock, 0, wx.ALL, 5 )

		self.Monitoring_Stock = wx.Button( self.m_panel, wx.ID_ANY, self.customString.monitor, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Monitoring_Stock, 0, wx.ALL, 5 )

		self.Setting = wx.Button( self.m_panel, wx.ID_ANY, self.customString.setting, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Setting, 0, wx.ALL, 5 )

		self.About_Us = wx.Button( self.m_panel, wx.ID_ANY, self.customString.about, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.About_Us, 0, wx.ALL, 5 )

		self.Admin = wx.Button( self.m_panel, wx.ID_ANY, self.customString.admin, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Admin, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel.SetSizer( bSizer1 )
		self.m_panel.Layout()
		bSizer1.Fit( self.m_panel )
		bSizerFrame.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizerFrame )
		self.Layout()

		# Connect Events
		self.bar.Bind( wx.EVT_TEXT_ENTER, self.onEnter )
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
	def onEnter( self, event ):
		event.Skip()

	def ExitOnButtonClick( self, event ):
		sys.exit(0)

	def onLogout( self, event ):
		self.Hide()
		Login.Show()

	def onHome( self, event ):
		self.Hide()
		Welcome.Show()

	def onNews( self, event ):
		self.Hide()
		finances.Show()

	def onSearch( self, event ):
		self.Hide()
		Search_Stock.Show()

	def onMonitoring( self, event ):
		self.Hide()
		Monitoring_stock.Show()

	def onSetting( self, event ):
		self.Setting = Setting(self)
		self.Setting.Show()

	def onAbout( self, event ):
		event.Skip()

	def onAdmin( self, event ):
		self.Hide()
		Admin.Show()