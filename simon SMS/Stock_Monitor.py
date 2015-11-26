# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class Login_frame_1
###########################################################################

class Login_frame_1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.lg_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.lg_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer301 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer93 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Login", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer93.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer301.Add( bSizer93, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer102 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer102.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer301.Add( bSizer102, 1, wx.EXPAND, 5 )
		
		bSizer100 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer181 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer181.SetFlexibleDirection( wx.BOTH )
		fgSizer181.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText51 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer181.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		self.m_textCtrl31 = wx.TextCtrl( self.lg_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl31.SetMinSize( wx.Size( 250,-1 ) )
		
		fgSizer181.Add( self.m_textCtrl31, 0, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		fgSizer181.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.m_textCtrl41 = wx.TextCtrl( self.lg_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl41.SetMinSize( wx.Size( 250,-1 ) )
		
		fgSizer181.Add( self.m_textCtrl41, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer100.Add( fgSizer181, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer301.Add( bSizer100, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer104 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.login = wx.Button( self.lg_panel, wx.ID_ANY, u"&Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer104.Add( self.login, 0, wx.ALL, 5 )
		
		self.register = wx.Button( self.lg_panel, wx.ID_ANY, u"&Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer104.Add( self.register, 0, wx.ALL, 5 )
		
		self.forgetPassword = wx.Button( self.lg_panel, wx.ID_ANY, u"&Forget Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer104.Add( self.forgetPassword, 0, wx.ALL, 5 )
		
		
		bSizer301.Add( bSizer104, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer66 = wx.BoxSizer( wx.VERTICAL )
		
		self.Exit = wx.Button( self.lg_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer66.Add( self.Exit, 0, wx.ALL, 5 )
		
		
		bSizer30.Add( bSizer66, 1, 0, 5 )
		
		bSizer65 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Setting = wx.Button( self.lg_panel, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer65.Add( self.Setting, 0, wx.ALL, 5 )
		
		self.About_Us = wx.Button( self.lg_panel, wx.ID_ANY, u"&About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer65.Add( self.About_Us, 0, wx.ALL, 5 )
		
		self.News = wx.Button( self.lg_panel, wx.ID_ANY, u"&News", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer65.Add( self.News, 0, wx.ALL, 5 )
		
		
		bSizer30.Add( bSizer65, 0, wx.EXPAND, 5 )
		
		
		bSizer301.Add( bSizer30, 0, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		
		self.lg_panel.SetSizer( bSizer301 )
		self.lg_panel.Layout()
		bSizer301.Fit( self.lg_panel )
		bSizerFrame.Add( self.lg_panel, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizerFrame )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.login.Bind( wx.EVT_BUTTON, self.onlogin )
		self.register.Bind( wx.EVT_BUTTON, self.onRegister )
		self.forgetPassword.Bind( wx.EVT_BUTTON, self.onForgetPassword )
		self.Exit.Bind( wx.EVT_BUTTON, self.onExit )
		self.Setting.Bind( wx.EVT_BUTTON, self.onSetting )
		self.About_Us.Bind( wx.EVT_BUTTON, self.onAboutUs )
		self.News.Bind( wx.EVT_BUTTON, self.onNews )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onlogin( self, event ):
		event.Skip()
	
	def onRegister( self, event ):
		event.Skip()
	
	def onForgetPassword( self, event ):
		event.Skip()
	
	def onExit( self, event ):
		event.Skip()
	
	def onSetting( self, event ):
		event.Skip()
	
	def onAboutUs( self, event ):
		event.Skip()
	
	def onNews( self, event ):
		event.Skip()
	

###########################################################################
## Class Home_Frame_2
###########################################################################

class Home_Frame_2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"News", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
	

###########################################################################
## Class News_Frame_3
###########################################################################

class News_Frame_3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"News", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.lg_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText24 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Finences News", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		self.m_staticText24.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer59.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		
		bSizer45.Add( bSizer59, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer54 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_richText2 = wx.richtext.RichTextCtrl( self.lg_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer54.Add( self.m_richText2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer45.Add( bSizer54, 1, wx.EXPAND, 5 )
		
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
		
		
		bSizer45.Add( bSizer301, 0, 0, 5 )
		
		
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
		self.Search_stock.Bind( wx.EVT_BUTTON, self.onSearch )
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
	

###########################################################################
## Class Search_stock_Frame_4
###########################################################################

class Search_stock_Frame_4 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Search Stock", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.lg_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText24 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Search Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		self.m_staticText24.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer59.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		
		bSizer45.Add( bSizer59, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer441 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer441.SetMinSize( wx.Size( -1,400 ) ) 
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText13 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Search Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer37.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_searchCtrl2 = wx.SearchCtrl( self.lg_panel, wx.ID_ANY, u"000001", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl2.ShowSearchButton( True )
		self.m_searchCtrl2.ShowCancelButton( True )
		bSizer37.Add( self.m_searchCtrl2, 1, wx.ALL, 5 )
		
		
		bSizer441.Add( bSizer37, 1, wx.EXPAND, 5 )
		
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		self.DisplaySearchResult = wx.Panel( self.lg_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.DisplaySearchResult.Enable( False )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		self.displaySearchResult = wx.richtext.RichTextCtrl( self.DisplaySearchResult, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.displaySearchResult.SetMinSize( wx.Size( -1,700 ) )
		
		bSizer39.Add( self.displaySearchResult, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.DisplaySearchResult.SetSizer( bSizer39 )
		self.DisplaySearchResult.Layout()
		bSizer39.Fit( self.DisplaySearchResult )
		bSizer38.Add( self.DisplaySearchResult, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer441.Add( bSizer38, 1, wx.EXPAND, 5 )
		
		
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
		self.m_searchCtrl2.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.Search )
		self.m_searchCtrl2.Bind( wx.EVT_TEXT_ENTER, self.Search )
		self.Exit.Bind( wx.EVT_BUTTON, self.ExitOnButtonClick )
		self.Home.Bind( wx.EVT_BUTTON, self.onLogin )
		self.News.Bind( wx.EVT_BUTTON, self.onNews )
		self.Search_stock.Bind( wx.EVT_BUTTON, self.onSearch )
		self.Monitoring_Stock.Bind( wx.EVT_BUTTON, self.onMonitoring )
		self.Setting.Bind( wx.EVT_BUTTON, self.onSetting )
		self.About_Us.Bind( wx.EVT_BUTTON, self.onAbout )
		self.Admin.Bind( wx.EVT_BUTTON, self.onAbout )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Search( self, event ):
		event.Skip()
	
	
	def ExitOnButtonClick( self, event ):
		event.Skip()
	
	def onLogin( self, event ):
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
		self.Monitoring_Stock.Bind( wx.EVT_BUTTON, self.onForgetPassword )
		self.Setting.Bind( wx.EVT_BUTTON, self.onForgetPassword )
		self.About_Us.Bind( wx.EVT_BUTTON, self.onForgetPassword )
		self.Admin.Bind( wx.EVT_BUTTON, self.onForgetPassword )
	
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
	
	def onForgetPassword( self, event ):
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
	

###########################################################################
## Class User_Admin
###########################################################################

class User_Admin ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer69 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer70 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer70.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.Admin_Search = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Admin_Search.ShowSearchButton( True )
		self.Admin_Search.ShowCancelButton( True )
		bSizer70.Add( self.Admin_Search, 0, wx.ALL, 5 )
		
		
		bSizer69.Add( bSizer70, 0, 0, 5 )
		
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		User_admin_displayChoices = []
		self.User_admin_display = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, User_admin_displayChoices, 0 )
		bSizer71.Add( self.User_admin_display, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer69.Add( bSizer71, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer69 )
		self.Layout()
		
		# Connect Events
		self.Admin_Search.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.Search )
		self.Admin_Search.Bind( wx.EVT_TEXT_ENTER, self.Search )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Search( self, event ):
		event.Skip()
	
	

###########################################################################
## Class Statistics
###########################################################################

class Statistics ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer72 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer73 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"STATISTICS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer73.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer72.Add( bSizer73, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer74 = wx.BoxSizer( wx.VERTICAL )
		
		statistics_displayChoices = []
		self.statistics_display = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, statistics_displayChoices, 0 )
		bSizer74.Add( self.statistics_display, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer72.Add( bSizer74, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer72 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Setting
###########################################################################

class Setting ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Setting", pos = wx.DefaultPosition, size = wx.Size( 632,511 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer75 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer77 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText31 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"System Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		self.m_staticText31.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer77.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer81 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_radioBox4Choices = [ u"Increase : Green; Decrease : Red", u"Increase : Red;    Decrease : Green" ]
		self.m_radioBox4 = wx.RadioBox( self.m_panel15, wx.ID_ANY, u"Arrow Color", wx.DefaultPosition, wx.DefaultSize, m_radioBox4Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox4.SetSelection( 1 )
		bSizer81.Add( self.m_radioBox4, 1, wx.ALL, 5 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel15, wx.ID_ANY, u"Monitoring Refresh Rate" ), wx.VERTICAL )
		
		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl13 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer55.Add( self.m_textCtrl13, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"sec/time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer55.Add( self.m_staticText24, 0, wx.TOP|wx.BOTTOM, 5 )
		
		
		sbSizer8.Add( bSizer55, 1, wx.EXPAND, 5 )
		
		self.m_button98 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"&Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_button98, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer81.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer77.Add( bSizer81, 0, wx.EXPAND, 5 )
		
		bSizer82 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText23 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Your Account", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		self.m_staticText23.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer82.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer83 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer87 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer96 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText32 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Account Stated", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		bSizer96.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer96.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		
		
		bSizer87.Add( bSizer96, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer99 = wx.BoxSizer( wx.VERTICAL )
		
		self.payButton = wx.Button( self.m_panel15, wx.ID_ANY, u"&PAY", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer99.Add( self.payButton, 0, wx.ALL, 5 )
		
		
		bSizer87.Add( bSizer99, 0, wx.ALIGN_RIGHT, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.VERTICAL )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText25 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"UID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer4.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.ID_ctrl1 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer4.Add( self.ID_ctrl1, 0, wx.ALL, 5 )
		
		self.m_staticText251 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Username:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText251.Wrap( -1 )
		fgSizer4.Add( self.m_staticText251, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.ID_ctrl = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer4.Add( self.ID_ctrl, 1, wx.ALL, 5 )
		
		self.OLDPassword = wx.StaticText( self.m_panel15, wx.ID_ANY, u"OLD Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OLDPassword.Wrap( -1 )
		fgSizer4.Add( self.OLDPassword, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.OPW_ctrl = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer4.Add( self.OPW_ctrl, 0, wx.ALL, 5 )
		
		self.New_Password = wx.StaticText( self.m_panel15, wx.ID_ANY, u"New Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.New_Password.Wrap( -1 )
		fgSizer4.Add( self.New_Password, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.NPW_ctrl = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer4.Add( self.NPW_ctrl, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Confirm New Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		fgSizer4.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.CNPW_ctrl = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer4.Add( self.CNPW_ctrl, 0, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Email:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		fgSizer4.Add( self.m_staticText35, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.email_ctrl = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.email_ctrl, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Telphone:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer4.Add( self.m_staticText36, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tel_ctrl = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.tel_ctrl, 0, wx.ALL, 5 )
		
		
		bSizer87.Add( fgSizer4, 0, 0, 5 )
		
		
		bSizer83.Add( bSizer87, 1, wx.EXPAND, 5 )
		
		
		bSizer82.Add( bSizer83, 1, wx.EXPAND, 5 )
		
		
		bSizer77.Add( bSizer82, 1, wx.EXPAND, 5 )
		
		bSizer85 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer86 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.save = wx.Button( self.m_panel15, wx.ID_ANY, u"&Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer86.Add( self.save, 0, wx.ALL, 5 )
		
		self.m_button95 = wx.Button( self.m_panel15, wx.ID_ANY, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer86.Add( self.m_button95, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer85.Add( bSizer86, 0, wx.ALIGN_RIGHT, 5 )
		
		
		bSizer77.Add( bSizer85, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel15.SetSizer( bSizer77 )
		self.m_panel15.Layout()
		bSizer77.Fit( self.m_panel15 )
		bSizer75.Add( self.m_panel15, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer75 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button98.Bind( wx.EVT_BUTTON, self.onRefreshTimeSummit )
		self.payButton.Bind( wx.EVT_BUTTON, self.onpay )
		self.save.Bind( wx.EVT_BUTTON, self.onSave )
		self.m_button95.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onRefreshTimeSummit( self, event ):
		event.Skip()
	
	def onpay( self, event ):
		event.Skip()
	
	def onSave( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	


###########################################################################
## Index Page
###########################################################################

class IndexPage ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY)
        self.Login_frame_1 = Login_frame_1.__init__( self, parent )
        self.Home_Frame_2 = Home_Frame_2.__init__( self, parent )
        self.News_Frame_3 = News_Frame_3.__init__( self, parent )
        self.Search_stock_Frame_4 = Search_stock_Frame_4.__init__( self, parent )
        self.Monitoring_Frame_5 = Monitoring_Frame_5.__init__( self, parent )
        self.Admin_6 = Admin_6.__init__( self, parent )
        #self.User_Admin = User_Admin (self)
        #self.Statistics = Statistics (self)
        #self.Setting = Setting (self)
        
        self.Home_Frame_2.Hide()
        self.News_Frame_3.Hide()
        self.Search_stock_Frame_4.Hide()
        self.Monitoring_Frame_5.Hide()
        self.Admin_6.Hide()
        #self.User_Admin.Hide()
        #self.Statistics.Hide()
        #self.Setting.Hide()