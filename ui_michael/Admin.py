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
## Class Admin
###########################################################################

class Admin ( wx.Panel ):

	def __init__( self, parent ):
		self.customString = customString('admin')
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.TAB_TRAVERSAL )

		self.SetMinSize( wx.Size( 900,600 ) )

		bSizerFrame = wx.BoxSizer( wx.VERTICAL )

		self.a_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		try:
			image_file = 'bg.jpg'
			bmp = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			self.bitmap = wx.StaticBitmap(self.a_panel, -1, bmp, (0,0))
		except IOError:
			raise SystemExit

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self.a_panel, wx.ID_ANY, self.customString.title, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )

		bSizer2.Add( self.title, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer3.SetMinSize( wx.Size( -1,400 ) )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.id_tit = wx.StaticText( self.a_panel, wx.ID_ANY, self.customString.id, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id_tit.Wrap( -1 )
		bSizer5.Add( self.id_tit, 0, wx.ALL, 5 )

		self.Admin_Search = wx.SearchCtrl( self.a_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Admin_Search.ShowSearchButton( True )
		self.Admin_Search.ShowCancelButton( True )
		bSizer5.Add( self.Admin_Search, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 0, 0, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		User_admin_displayChoices = []
		self.User_admin_display = wx.CheckListBox( self.a_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, User_admin_displayChoices, 0 )
		bSizer6.Add( self.User_admin_display, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.static_tit = wx.StaticText( self.a_panel, wx.ID_ANY, self.customString.stat, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.static_tit.Wrap( -1 )
		self.static_tit.SetFont( wx.Font( 17, 70, 90, 90, False, wx.EmptyString ) )

		bSizer8.Add( self.static_tit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer7.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		statistics_displayChoices = []
		self.statistics_display = wx.CheckListBox( self.a_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, statistics_displayChoices, 0 )
		bSizer9.Add( self.statistics_display, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.Exit = wx.Button( self.a_panel, wx.ID_ANY, self.customString.exit, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Exit, 0, wx.ALL, 5 )

		self.Logout = wx.Button( self.a_panel, wx.ID_ANY, self.customString.logout, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Logout, 0, wx.ALL, 5 )

		self.Home = wx.Button( self.a_panel, wx.ID_ANY, self.customString.home, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Home, 0, wx.ALL, 5 )

		self.News = wx.Button( self.a_panel, wx.ID_ANY, self.customString.news, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.News, 0, wx.ALL, 5 )

		self.Search_stock = wx.Button( self.a_panel, wx.ID_ANY, self.customString.search, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Search_stock, 0, wx.ALL, 5 )

		self.Monitoring_Stock = wx.Button( self.a_panel, wx.ID_ANY, self.customString.monitor, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Monitoring_Stock, 0, wx.ALL, 5 )

		self.Setting = wx.Button( self.a_panel, wx.ID_ANY, self.customString.setting, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Setting, 0, wx.ALL, 5 )

		self.About_Us = wx.Button( self.a_panel, wx.ID_ANY, self.customString.about, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.About_Us, 0, wx.ALL, 5 )

		self.Admin1 = wx.Button( self.a_panel, wx.ID_ANY, self.customString.admin, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Admin1, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.a_panel.SetSizer( bSizer1 )
		self.a_panel.Layout()
		bSizer1.Fit( self.a_panel )
		bSizerFrame.Add( self.a_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizerFrame )
		self.Layout()

		# Connect Events
		self.Admin_Search.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.onSearchID )
		self.Admin_Search.Bind( wx.EVT_TEXT_ENTER, self.onSearchID )
		self.Exit.Bind( wx.EVT_BUTTON, self.ExitOnButtonClick )
		self.Logout.Bind( wx.EVT_BUTTON, self.onLogout )
		self.Home.Bind( wx.EVT_BUTTON, self.onHome )
		self.News.Bind( wx.EVT_BUTTON, self.onNews )
		self.Search_stock.Bind( wx.EVT_BUTTON, self.onSearch )
		self.Monitoring_Stock.Bind( wx.EVT_BUTTON, self.onMonitoring )
		self.Setting.Bind( wx.EVT_BUTTON, self.onSetting )
		self.About_Us.Bind( wx.EVT_BUTTON, self.onAbout )
		self.Admin1.Bind( wx.EVT_BUTTON, self.onAdmin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onSearchID( self, event ):
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