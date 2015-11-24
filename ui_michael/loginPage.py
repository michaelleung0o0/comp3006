import os
import wx
import wx.xrc
import wx.richtext
import Setting
###########################################################################
## Class Login_frame_1
###########################################################################

class Login_frame_1 ( wx.Frame ):

	# def __init__( self, parent ):
		# wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
	def __init__(self, *arg, **kwargs):
		super(Login_frame_1, self).__init__(*arg, **kwargs)

		# this.parent = parent

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
		# event.Skip()
		self.Close()

	def onSetting( self, event ):
		# event.Skip()
		os.system('python Setting.py')
		# Setting.Setting.__init__( self )

	def onAboutUs( self, event ):
		event.Skip()

	def onNews( self, event ):
		event.Skip()