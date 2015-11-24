import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class Setting
###########################################################################

class Setting ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Setting", pos = wx.DefaultPosition, size = wx.Size( 632,511 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
	# def __init__(self, *arg, **kwargs):
		# super(Setting, self).__init__(*arg, **kwargs)

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