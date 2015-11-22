# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Login_frame
###########################################################################

class Login_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.lg_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		gSizer12 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer23.Add( bSizer31, 1, wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		self.Exit = wx.Button( self.lg_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.Exit, 0, wx.ALL, 5 )
		
		
		gSizer12.Add( bSizer23, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		gSizer13 = wx.GridSizer( 3, 0, 0, 0 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer27.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Login", wx.Point( -1,-1 ), wx.Size( 65,30 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 20, 72, 90, 90, False, wx.EmptyString ) )
		
		bSizer27.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		gSizer13.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		fgSizer18 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText5 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer18.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.lg_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer18.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self.lg_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer13.Add( fgSizer18, 1, wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Login = wx.Button( self.lg_panel, wx.ID_ANY, u"&Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.Login, 0, wx.ALL, 5 )
		
		self.Register = wx.Button( self.lg_panel, wx.ID_ANY, u"&Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.Register, 0, wx.ALL, 5 )
		
		self.Forget = wx.Button( self.lg_panel, wx.ID_ANY, u"&Forget password", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.Forget, 0, wx.ALL, 5 )
		
		
		gSizer13.Add( bSizer30, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		
		gSizer12.Add( gSizer13, 1, wx.EXPAND, 5 )
		
		
		self.lg_panel.SetSizer( gSizer12 )
		self.lg_panel.Layout()
		gSizer12.Fit( self.lg_panel )
		bSizerFrame.Add( self.lg_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizerFrame )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Exit.Bind( wx.EVT_BUTTON, self.onExit )
		self.Login.Bind( wx.EVT_BUTTON, self.onLogin )
		self.Register.Bind( wx.EVT_BUTTON, self.onRegister )
		self.Forget.Bind( wx.EVT_BUTTON, self.onForgetPassword )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onExit( self, event ):
		event.Skip()
	
	def onLogin( self, event ):
		event.Skip()
	
	def onRegister( self, event ):
		event.Skip()
	
	def onForgetPassword( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer42.Add( self.m_staticText7, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button23 = wx.Button( self.m_panel2, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.m_button23, 1, wx.ALL, 5 )
		
		
		fgSizer19.Add( bSizer42, 1, wx.EXPAND, 5 )
		
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer43.Add( self.m_staticText8, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button24 = wx.Button( self.m_panel2, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.m_button24, 0, wx.ALL, 5 )
		
		
		fgSizer19.Add( bSizer43, 1, wx.EXPAND, 5 )
		
		
		bSizer40.Add( fgSizer19, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer40 )
		self.m_panel2.Layout()
		bSizer40.Fit( self.m_panel2 )
		bSizer39.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer39 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 636,372 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizerFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.lg_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		gSizer12 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Login", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 20, 72, 90, 90, False, wx.EmptyString ) )
		
		gSizer12.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		gSizer13 = wx.GridSizer( 2, 0, 0, 0 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer27.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer13.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		fgSizer18 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText5 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer18.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.lg_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.lg_panel, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer18.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self.lg_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer13.Add( fgSizer18, 1, wx.EXPAND, 5 )
		
		bSizer271 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer13.Add( bSizer271, 1, wx.EXPAND, 5 )
		
		bSizer302 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Register1 = wx.Button( self.lg_panel, wx.ID_ANY, u"&Register", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer302.Add( self.Register1, 0, wx.ALL, 5 )
		
		self.Login1 = wx.Button( self.lg_panel, wx.ID_ANY, u"&Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer302.Add( self.Login1, 0, wx.ALL, 5 )
		
		self.Forget1 = wx.Button( self.lg_panel, wx.ID_ANY, u"&Forget password", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer302.Add( self.Forget1, 0, wx.ALL, 5 )
		
		
		gSizer13.Add( bSizer302, 1, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER, 5 )
		
		
		gSizer12.Add( gSizer13, 1, wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Exit = wx.Button( self.lg_panel, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.Exit, 0, wx.ALL, 5 )
		
		self.Home = wx.Button( self.lg_panel, wx.ID_ANY, u"&Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.Home, 0, wx.ALL, 5 )
		
		self.Search stock = wx.Button( self.lg_panel, wx.ID_ANY, u"Search stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.Search stock, 0, wx.ALL, 5 )
		
		self.Monitoring Stock = wx.Button( self.lg_panel, wx.ID_ANY, u"Monitoring Stock", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.Monitoring Stock, 0, wx.ALL, 5 )
		
		self.Setting = wx.Button( self.lg_panel, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.Setting, 0, wx.ALL, 5 )
		
		self.About Us = wx.Button( self.lg_panel, wx.ID_ANY, u"About Us", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.About Us, 0, wx.ALL, 5 )
		
		self.Admin = wx.Button( self.lg_panel, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.Admin, 0, wx.ALL, 5 )
		
		
		gSizer12.Add( bSizer30, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		
		self.lg_panel.SetSizer( gSizer12 )
		self.lg_panel.Layout()
		gSizer12.Fit( self.lg_panel )
		bSizerFrame.Add( self.lg_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer301 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizerFrame.Add( bSizer301, 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizerFrame, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer10 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Register1.Bind( wx.EVT_BUTTON, self.onRegister )
		self.Login1.Bind( wx.EVT_BUTTON, self.onLogin )
		self.Forget1.Bind( wx.EVT_BUTTON, self.onForgetPassword )
		self.Exit.Bind( wx.EVT_BUTTON, self.ExitOnButtonClick )
		self.Home.Bind( wx.EVT_BUTTON, self.onLogin )
		self.Search stock.Bind( wx.EVT_BUTTON, self.onRegister )
		self.Monitoring Stock.Bind( wx.EVT_BUTTON, self.onForgetPassword )
		self.Setting.Bind( wx.EVT_BUTTON, self.onForgetPassword )
		self.About Us.Bind( wx.EVT_BUTTON, self.onForgetPassword )
		self.Admin.Bind( wx.EVT_BUTTON, self.onForgetPassword )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onRegister( self, event ):
		event.Skip()
	
	def onLogin( self, event ):
		event.Skip()
	
	def onForgetPassword( self, event ):
		event.Skip()
	
	def ExitOnButtonClick( self, event ):
		event.Skip()
	
	
	
	
	
	
	

