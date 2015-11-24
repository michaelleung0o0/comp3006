import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class Monitoring_Frame_5
###########################################################################

class Monitoring_Frame_5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Monitoring Stock", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizerFrame = wx.BoxSizer( wx.VERTICAL )

		self.lg_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Welcome", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		self.m_staticText24.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )

		bSizer59.Add( self.m_staticText24, 0, wx.ALL, 5 )


		bSizer45.Add( bSizer59, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer441 = wx.BoxSizer( wx.VERTICAL )

		bSizer441.SetMinSize( wx.Size( -1,400 ) )

		bSizer441.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer45.Add( bSizer441, 1, wx.EXPAND, 5 )

		bSizer301 = wx.BoxSizer( wx.HORIZONTAL )

		self.Exit = wx.Button( self.lg_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Exit, 0, wx.ALL, 5 )

		self.Home = wx.Button( self.lg_panel, wx.ID_ANY, u"&Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Home, 0, wx.ALL, 5 )

		self.News = wx.Button( self.lg_panel, wx.ID_ANY, u"&News", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.News, 0, wx.ALL, 5 )

		self.Search_stock = wx.Button( self.lg_panel, wx.ID_ANY, u"Search stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Search_stock, 0, wx.ALL, 5 )

		self.Monitoring_Stock = wx.Button( self.lg_panel, wx.ID_ANY, u"Monitoring Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Monitoring_Stock, 0, wx.ALL, 5 )

		self.Setting = wx.Button( self.lg_panel, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Setting, 0, wx.ALL, 5 )

		self.About_Us = wx.Button( self.lg_panel, wx.ID_ANY, u"About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.About_Us, 0, wx.ALL, 5 )

		self.Admin = wx.Button( self.lg_panel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Admin, 0, wx.ALL, 5 )


		bSizer45.Add( bSizer301, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.lg_panel.SetSizer( bSizer45 )
		self.lg_panel.Layout()
		bSizer45.Fit( self.lg_panel )
		bSizerFrame.Add( self.lg_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizerFrame )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Exit.Bind( wx.EVT_BUTTON, self.ExitOnButtonClick )
		self.Home.Bind( wx.EVT_BUTTON, self.onLogin )
		self.News.Bind( wx.EVT_BUTTON, self.onNews )
		self.Search_stock.Bind( wx.EVT_BUTTON, self.onRegister )
		self.Monitoring_Stock.Bind( wx.EVT_BUTTON, self.onMonitoring )
		self.Setting.Bind( wx.EVT_BUTTON, self.onSetting )
		self.About_Us.Bind( wx.EVT_BUTTON, self.onAbout )
		self.Admin.Bind( wx.EVT_BUTTON, self.onAdmin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ExitOnButtonClick( self, event ):
		event.Skip()

	def onLogin( self, event ):
		event.Skip()

	def onNews( self, event ):
		event.Skip()

	def onRegister( self, event ):
		event.Skip()

	def onMonitoring( self, event ):
		event.Skip()

	def onSetting( self, event ):
		event.Skip()

	def onAbout( self, event ):
		event.Skip()

	def onAdmin( self, event ):
		event.Skip()


###########################################################################
## Class Admin_6
###########################################################################

class Admin_6 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"News", pos = wx.DefaultPosition, size = wx.Size( 1052,736 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizerFrame = wx.BoxSizer( wx.VERTICAL )

		self.lg_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		self.m_staticText24.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )

		bSizer59.Add( self.m_staticText24, 0, wx.ALL, 5 )


		bSizer45.Add( bSizer59, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer441 = wx.BoxSizer( wx.VERTICAL )

		bSizer441.SetMinSize( wx.Size( -1,400 ) )
		self.m_choicebook2 = wx.Choicebook( self.lg_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		bSizer441.Add( self.m_choicebook2, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer45.Add( bSizer441, 1, wx.EXPAND, 5 )

		bSizer301 = wx.BoxSizer( wx.HORIZONTAL )

		self.Exit = wx.Button( self.lg_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Exit, 0, wx.ALL, 5 )

		self.Home = wx.Button( self.lg_panel, wx.ID_ANY, u"&Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Home, 0, wx.ALL, 5 )

		self.News = wx.Button( self.lg_panel, wx.ID_ANY, u"&News", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.News, 0, wx.ALL, 5 )

		self.Search_Stock = wx.Button( self.lg_panel, wx.ID_ANY, u"Search stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Search_Stock, 0, wx.ALL, 5 )

		self.Monitoring_Stock = wx.Button( self.lg_panel, wx.ID_ANY, u"Monitoring Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Monitoring_Stock, 0, wx.ALL, 5 )

		self.Setting = wx.Button( self.lg_panel, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Setting, 0, wx.ALL, 5 )

		self.About_Us = wx.Button( self.lg_panel, wx.ID_ANY, u"About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.About_Us, 0, wx.ALL, 5 )

		self.Admin = wx.Button( self.lg_panel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer301.Add( self.Admin, 0, wx.ALL, 5 )


		bSizer45.Add( bSizer301, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.lg_panel.SetSizer( bSizer45 )
		self.lg_panel.Layout()
		bSizer45.Fit( self.lg_panel )
		bSizerFrame.Add( self.lg_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizerFrame )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_choicebook2.Bind( wx.EVT_CHOICEBOOK_PAGE_CHANGED, self.DisplayPage )
		self.Exit.Bind( wx.EVT_BUTTON, self.ExitOnButtonClick )
		self.Home.Bind( wx.EVT_BUTTON, self.onLogin )
		self.News.Bind( wx.EVT_BUTTON, self.onNews )
		self.Search_Stock.Bind( wx.EVT_BUTTON, self.onSearch )
		self.Monitoring_Stock.Bind( wx.EVT_BUTTON, self.onMonitioring )
		self.Setting.Bind( wx.EVT_BUTTON, self.onSetting )
		self.About_Us.Bind( wx.EVT_BUTTON, self.onAbout )
		self.Admin.Bind( wx.EVT_BUTTON, self.onAdmin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def DisplayPage( self, event ):
		event.Skip()

	def ExitOnButtonClick( self, event ):
		event.Skip()

	def onLogin( self, event ):
		event.Skip()

	def onNews( self, event ):
		event.Skip()

	def onSearch( self, event ):
		event.Skip()

	def onMonitioring( self, event ):
		event.Skip()

	def onSetting( self, event ):
		event.Skip()

	def onAbout( self, event ):
		event.Skip()

	def onAdmin( self, event ):
		event.Skip()
