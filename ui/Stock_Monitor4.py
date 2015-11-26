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
## Class Login
###########################################################################

class Login ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.TAB_TRAVERSAL )
		
		self.SetMinSize( wx.Size( 900,600 ) )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.lg_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.lg_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Login", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 36, 74, 90, 92, False, "Arial" ) )
		
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
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
		
		
		bSizer4.Add( fgSizer181, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer4, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.login = wx.Button( self.lg_panel, wx.ID_ANY, u"&Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.login, 0, wx.ALL, 5 )
		
		self.register = wx.Button( self.lg_panel, wx.ID_ANY, u"&Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.register, 0, wx.ALL, 5 )
		
		self.forgetPassword = wx.Button( self.lg_panel, wx.ID_ANY, u"&Forget Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.forgetPassword, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.Exit = wx.Button( self.lg_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Exit, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer7, 1, 0, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Setting = wx.Button( self.lg_panel, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.Setting, 0, wx.ALL, 5 )
		
		self.About_Us = wx.Button( self.lg_panel, wx.ID_ANY, u"&About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.About_Us, 0, wx.ALL, 5 )
		
		self.News = wx.Button( self.lg_panel, wx.ID_ANY, u"&News", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.News, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer6, 0, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		
		self.lg_panel.SetSizer( bSizer1 )
		self.lg_panel.Layout()
		bSizer1.Fit( self.lg_panel )
		bSizerFrame.Add( self.lg_panel, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizerFrame )
		self.Layout()
		
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
## Class Welcome
###########################################################################

class Welcome ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.TAB_TRAVERSAL )
		
		self.SetMinSize( wx.Size( 900,600 ) )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.w_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self.w_panel, wx.ID_ANY, u"Welcome", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer59.Add( self.title, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer59, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2.SetMinSize( wx.Size( -1,400 ) ) 
		self.w_page = wx.TextCtrl( self.w_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RICH|wx.TE_RICH2|wx.TE_WORDWRAP )
		bSizer2.Add( self.w_page, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
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
	
	def onLogout( self, event ):
		event.Skip()
	
	def onHome( self, event ):
		event.Skip()
	
	def onNews( self, event ):
		event.Skip()
	
	def onRegister( self, event ):
		event.Skip()
	
	def onForgetPassword( self, event ):
		event.Skip()
	
	
	
	

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
	

###########################################################################
## Class Search_Stock
###########################################################################

class Search_Stock ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.TAB_TRAVERSAL )
		
		self.SetMinSize( wx.Size( 900,600 ) )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.s_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self.s_panel, wx.ID_ANY, u"Search Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.title, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.search_tit = wx.StaticText( self.s_panel, wx.ID_ANY, u"Search Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_tit.Wrap( -1 )
		bSizer4.Add( self.search_tit, 0, wx.ALL, 5 )
		
		self.search_box = wx.SearchCtrl( self.s_panel, wx.ID_ANY, u"000001", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_box.ShowSearchButton( True )
		self.search_box.ShowCancelButton( True )
		bSizer4.Add( self.search_box, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer64 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl2 = wx.ListCtrl( self.s_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST )
		bSizer64.Add( self.m_listCtrl2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer64, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Exit = wx.Button( self.s_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Exit, 0, wx.ALL, 5 )
		
		self.Logout = wx.Button( self.s_panel, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Logout, 0, wx.ALL, 5 )
		
		self.Home = wx.Button( self.s_panel, wx.ID_ANY, u"&Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Home, 0, wx.ALL, 5 )
		
		self.News = wx.Button( self.s_panel, wx.ID_ANY, u"&News", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.News, 0, wx.ALL, 5 )
		
		self.Search_stock = wx.Button( self.s_panel, wx.ID_ANY, u"Search stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Search_stock, 0, wx.ALL, 5 )
		
		self.Monitoring_Stock = wx.Button( self.s_panel, wx.ID_ANY, u"Monitoring Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Monitoring_Stock, 0, wx.ALL, 5 )
		
		self.Setting = wx.Button( self.s_panel, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Setting, 0, wx.ALL, 5 )
		
		self.About_Us = wx.Button( self.s_panel, wx.ID_ANY, u"About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.About_Us, 0, wx.ALL, 5 )
		
		self.Admin = wx.Button( self.s_panel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Admin, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.s_panel.SetSizer( bSizer1 )
		self.s_panel.Layout()
		bSizer1.Fit( self.s_panel )
		bSizerFrame.Add( self.s_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizerFrame )
		self.Layout()
		
		# Connect Events
		self.search_box.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.onSearch )
		self.search_box.Bind( wx.EVT_TEXT_ENTER, self.onSearch )
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
	def onSearch( self, event ):
		event.Skip()
	
	
	def ExitOnButtonClick( self, event ):
		event.Skip()
	
	def onLogout( self, event ):
		event.Skip()
	
	def onHome( self, event ):
		event.Skip()
	
	def onNews( self, event ):
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
## Class Monitoring_stock
###########################################################################

class Monitoring_stock ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.TAB_TRAVERSAL )
		
		self.SetMinSize( wx.Size( 900,600 ) )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self.m_panel, wx.ID_ANY, u"Monitoring Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.title, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3.SetMinSize( wx.Size( -1,400 ) ) 
		self.m_listCtrl1 = wx.ListCtrl( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST )
		bSizer3.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.bar = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.bar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Exit = wx.Button( self.m_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Exit, 0, wx.ALL, 5 )
		
		self.Logout = wx.Button( self.m_panel, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Logout, 0, wx.ALL, 5 )
		
		self.Home = wx.Button( self.m_panel, wx.ID_ANY, u"&Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Home, 0, wx.ALL, 5 )
		
		self.News = wx.Button( self.m_panel, wx.ID_ANY, u"&News", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.News, 0, wx.ALL, 5 )
		
		self.Search_stock = wx.Button( self.m_panel, wx.ID_ANY, u"Search stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Search_stock, 0, wx.ALL, 5 )
		
		self.Monitoring_Stock = wx.Button( self.m_panel, wx.ID_ANY, u"Monitoring Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Monitoring_Stock, 0, wx.ALL, 5 )
		
		self.Setting = wx.Button( self.m_panel, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.Setting, 0, wx.ALL, 5 )
		
		self.About_Us = wx.Button( self.m_panel, wx.ID_ANY, u"About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.About_Us, 0, wx.ALL, 5 )
		
		self.Admin = wx.Button( self.m_panel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
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
	

###########################################################################
## Class Admin
###########################################################################

class Admin ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.TAB_TRAVERSAL )
		
		self.SetMinSize( wx.Size( 900,600 ) )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.a_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self.a_panel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.title, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer3.SetMinSize( wx.Size( -1,400 ) ) 
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.id_tit = wx.StaticText( self.a_panel, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		self.static_tit = wx.StaticText( self.a_panel, wx.ID_ANY, u"STATISTICS", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		self.Exit = wx.Button( self.a_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Exit, 0, wx.ALL, 5 )
		
		self.Logout = wx.Button( self.a_panel, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Logout, 0, wx.ALL, 5 )
		
		self.Home = wx.Button( self.a_panel, wx.ID_ANY, u"&Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Home, 0, wx.ALL, 5 )
		
		self.News = wx.Button( self.a_panel, wx.ID_ANY, u"&News", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.News, 0, wx.ALL, 5 )
		
		self.Search_stock = wx.Button( self.a_panel, wx.ID_ANY, u"Search stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Search_stock, 0, wx.ALL, 5 )
		
		self.Monitoring_Stock = wx.Button( self.a_panel, wx.ID_ANY, u"Monitoring Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Monitoring_Stock, 0, wx.ALL, 5 )
		
		self.Setting = wx.Button( self.a_panel, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.Setting, 0, wx.ALL, 5 )
		
		self.About_Us = wx.Button( self.a_panel, wx.ID_ANY, u"About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.About_Us, 0, wx.ALL, 5 )
		
		self.Admin1 = wx.Button( self.a_panel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
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
	

###########################################################################
## Class Forget_password
###########################################################################

class Forget_password ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Forget Password", pos = wx.DefaultPosition, size = wx.Size( 500,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 500,200 ), wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.f_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self.f_panel, wx.ID_ANY, u"Forget Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.id = wx.StaticText( self.f_panel, wx.ID_ANY, u"ID: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id.Wrap( -1 )
		fgSizer.Add( self.id, 0, wx.ALL, 5 )
		
		self.id_box = wx.TextCtrl( self.f_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id_box.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer.Add( self.id_box, 0, wx.ALL, 5 )
		
		self.email = wx.StaticText( self.f_panel, wx.ID_ANY, u"Email: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )
		fgSizer.Add( self.email, 0, wx.ALL, 5 )
		
		self.email_box = wx.TextCtrl( self.f_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email_box.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer.Add( self.email_box, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.reset_password = wx.Button( self.f_panel, wx.ID_ANY, u"&Reset Password ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.reset_password, 0, wx.ALL, 5 )
		
		self.Contect_Admin = wx.Button( self.f_panel, wx.ID_ANY, u"&Contect Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Contect_Admin, 0, wx.ALL, 5 )
		
		self.cancel = wx.Button( self.f_panel, wx.ID_ANY, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.cancel, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.f_panel.SetSizer( bSizer1 )
		self.f_panel.Layout()
		bSizer1.Fit( self.f_panel )
		bSizer.Add( self.f_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.reset_password.Bind( wx.EVT_BUTTON, self.onReset )
		self.Contect_Admin.Bind( wx.EVT_BUTTON, self.onContect )
		self.cancel.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onReset( self, event ):
		event.Skip()
	
	def onContect( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Register
###########################################################################

class Register ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Register", pos = wx.DefaultPosition, size = wx.Size( 500,320 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.r_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self.r_panel, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer.SetFlexibleDirection( wx.VERTICAL )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.id = wx.StaticText( self.r_panel, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id.Wrap( -1 )
		fgSizer.Add( self.id, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.ID_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer.Add( self.ID_ctrl, 1, wx.ALL, 5 )
		
		self.OLD_Password = wx.StaticText( self.r_panel, wx.ID_ANY, u"OLD Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OLD_Password.Wrap( -1 )
		fgSizer.Add( self.OLD_Password, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.OPW_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer.Add( self.OPW_ctrl, 1, wx.ALL, 5 )
		
		self.n_p = wx.StaticText( self.r_panel, wx.ID_ANY, u"New Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.n_p.Wrap( -1 )
		fgSizer.Add( self.n_p, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.NPW_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer.Add( self.NPW_ctrl, 0, wx.ALL, 5 )
		
		self.c_p = wx.StaticText( self.r_panel, wx.ID_ANY, u"Confirm New Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_p.Wrap( -1 )
		fgSizer.Add( self.c_p, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.CNPW_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer.Add( self.CNPW_ctrl, 0, wx.ALL, 5 )
		
		self.email = wx.StaticText( self.r_panel, wx.ID_ANY, u"Email:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )
		fgSizer.Add( self.email, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.email_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.email_ctrl, 0, wx.ALL, 5 )
		
		self.tel = wx.StaticText( self.r_panel, wx.ID_ANY, u"Telphone:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tel.Wrap( -1 )
		fgSizer.Add( self.tel, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tel_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.tel_ctrl, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer86 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.save = wx.Button( self.r_panel, wx.ID_ANY, u"&Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer86.Add( self.save, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cancel = wx.Button( self.r_panel, wx.ID_ANY, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer86.Add( self.cancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2.Add( bSizer86, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		self.r_panel.SetSizer( bSizer1 )
		self.r_panel.Layout()
		bSizer1.Fit( self.r_panel )
		bSizer.Add( self.r_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.save.Bind( wx.EVT_BUTTON, self.onSave )
		self.cancel.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSave( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Setting
###########################################################################

class Setting ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Setting", pos = wx.DefaultPosition, size = wx.Size( 632,511 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.setting_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self.setting_panel, wx.ID_ANY, u"System Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		ArrowColorChoices = [ u"Positive : Green; Negative : Red", u"Positive : Red; Negative : Green" ]
		self.ArrowColor = wx.RadioBox( self.setting_panel, wx.ID_ANY, u"Arrow Color", wx.DefaultPosition, wx.DefaultSize, ArrowColorChoices, 1, wx.RA_SPECIFY_COLS )
		self.ArrowColor.SetSelection( 0 )
		bSizer2.Add( self.ArrowColor, 1, wx.ALL, 5 )
		
		time = wx.StaticBoxSizer( wx.StaticBox( self.setting_panel, wx.ID_ANY, u"Refresh time" ), wx.HORIZONTAL )
		
		timeChoices = [ u"0.5 seconds", u"1    seconds", u"2    seconds" ]
		self.time = wx.Choice( time.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, timeChoices, 0 )
		self.time.SetSelection( 0 )
		time.Add( self.time, 0, wx.ALL, 5 )
		
		self.submit = wx.Button( time.GetStaticBox(), wx.ID_ANY, u"&Summits", wx.DefaultPosition, wx.DefaultSize, 0 )
		time.Add( self.submit, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( time, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Acc = wx.StaticText( self.setting_panel, wx.ID_ANY, u"Account Stated", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Acc.Wrap( -1 )
		bSizer6.Add( self.Acc, 0, wx.ALL, 5 )
		
		self.state = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer6.Add( self.state, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer6, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.payButton = wx.Button( self.setting_panel, wx.ID_ANY, u"&PAY", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.payButton, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer7, 0, wx.ALIGN_RIGHT, 5 )
		
		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.VERTICAL )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.id = wx.StaticText( self.setting_panel, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id.Wrap( -1 )
		fgSizer8.Add( self.id, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.ID_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer8.Add( self.ID_ctrl, 1, wx.ALL, 5 )
		
		self.OLD_Password = wx.StaticText( self.setting_panel, wx.ID_ANY, u"OLD Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OLD_Password.Wrap( -1 )
		fgSizer8.Add( self.OLD_Password, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.OPW_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer8.Add( self.OPW_ctrl, 0, wx.ALL, 5 )
		
		self.new_p = wx.StaticText( self.setting_panel, wx.ID_ANY, u"New Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.new_p.Wrap( -1 )
		fgSizer8.Add( self.new_p, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.NPW_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer8.Add( self.NPW_ctrl, 0, wx.ALL, 5 )
		
		self.c_p = wx.StaticText( self.setting_panel, wx.ID_ANY, u"Confirm New Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_p.Wrap( -1 )
		fgSizer8.Add( self.c_p, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.CNPW_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer8.Add( self.CNPW_ctrl, 0, wx.ALL, 5 )
		
		self.email = wx.StaticText( self.setting_panel, wx.ID_ANY, u"Email:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )
		fgSizer8.Add( self.email, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.email_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.email_ctrl, 0, wx.ALL, 5 )
		
		self.tel = wx.StaticText( self.setting_panel, wx.ID_ANY, u"Telphone:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tel.Wrap( -1 )
		fgSizer8.Add( self.tel, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.tel_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.tel_ctrl, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( fgSizer8, 0, 0, 5 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.save = wx.Button( self.setting_panel, wx.ID_ANY, u"&Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.save, 0, wx.ALL, 5 )
		
		self.m_button95 = wx.Button( self.setting_panel, wx.ID_ANY, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button95, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer8.Add( bSizer9, 0, wx.ALIGN_RIGHT, 5 )
		
		
		bSizer1.Add( bSizer8, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.setting_panel.SetSizer( bSizer1 )
		self.setting_panel.Layout()
		bSizer1.Fit( self.setting_panel )
		bSizer.Add( self.setting_panel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.submit.Bind( wx.EVT_BUTTON, self.onRefreshTimeSummit )
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
## Class About_Us
###########################################################################

class About_Us ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About Us", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer62 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer63 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText30 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		self.m_staticText30.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer63.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_richText3 = wx.richtext.RichTextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer63.Add( self.m_richText3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.exit = wx.Button( self.m_panel11, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer63.Add( self.exit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel11.SetSizer( bSizer63 )
		self.m_panel11.Layout()
		bSizer63.Fit( self.m_panel11 )
		bSizer62.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer62 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.exit.Bind( wx.EVT_BUTTON, self.onExit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onExit( self, event ):
		event.Skip()
	

