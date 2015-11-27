import wx
import wx.xrc
import wx.richtext
import sys
from customString import customString

###########################################################################
## Class Setting
###########################################################################

class Setting ( wx.Frame ):

	def __init__( self, parent ):
		self.customString = customString('setting')
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = self.customString.title, pos = wx.DefaultPosition, size = wx.Size( 632,511 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		self.setting_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self.setting_panel, wx.ID_ANY, self.customString.setTitle, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )

		bSizer1.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		ArrowColorChoices = [ self.customString.arrow1, self.customString.arrow2]
		self.ArrowColor = wx.RadioBox( self.setting_panel, wx.ID_ANY, self.customString.acolor, wx.DefaultPosition, wx.DefaultSize, ArrowColorChoices, 1, wx.RA_SPECIFY_COLS )
		self.ArrowColor.SetSelection( 0 )
		bSizer2.Add( self.ArrowColor, 1, wx.ALL, 5 )

		time = wx.StaticBoxSizer( wx.StaticBox( self.setting_panel, wx.ID_ANY, self.customString.rtime ), wx.HORIZONTAL )

		timeChoices = [ self.customString.halfsec, self.customString.onesec, self.customString.twosec ]
		self.time = wx.Choice( time.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, timeChoices, 0 )
		self.time.SetSelection( 0 )
		time.Add( self.time, 0, wx.ALL, 5 )

		self.submit = wx.Button( time.GetStaticBox(), wx.ID_ANY, self.customString.apply, wx.DefaultPosition, wx.DefaultSize, 0 )
		time.Add( self.submit, 0, wx.ALL, 5 )


		bSizer2.Add( time, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.Acc = wx.StaticText( self.setting_panel, wx.ID_ANY, self.customString. accstat, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Acc.Wrap( -1 )
		bSizer6.Add( self.Acc, 0, wx.ALL, 5 )

		self.state = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer6.Add( self.state, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer6, 0, wx.ALIGN_RIGHT, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.payButton = wx.Button( self.setting_panel, wx.ID_ANY, self.customString.pay, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.payButton, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer7, 0, wx.ALIGN_RIGHT, 5 )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.VERTICAL )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.id = wx.StaticText( self.setting_panel, wx.ID_ANY, self.customString.id, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id.Wrap( -1 )
		fgSizer8.Add( self.id, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.ID_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer8.Add( self.ID_ctrl, 1, wx.ALL, 5 )

		self.OLD_Password = wx.StaticText( self.setting_panel, wx.ID_ANY, self.customString.oldpw, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OLD_Password.Wrap( -1 )
		fgSizer8.Add( self.OLD_Password, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.OPW_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer8.Add( self.OPW_ctrl, 0, wx.ALL, 5 )

		self.new_p = wx.StaticText( self.setting_panel, wx.ID_ANY, self.customString.newpw, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.new_p.Wrap( -1 )
		fgSizer8.Add( self.new_p, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.NPW_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer8.Add( self.NPW_ctrl, 0, wx.ALL, 5 )

		self.c_p = wx.StaticText( self.setting_panel, wx.ID_ANY, self.customString.cpw, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_p.Wrap( -1 )
		fgSizer8.Add( self.c_p, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.CNPW_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer8.Add( self.CNPW_ctrl, 0, wx.ALL, 5 )

		self.email = wx.StaticText( self.setting_panel, wx.ID_ANY, self.customString.email, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )
		fgSizer8.Add( self.email, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.email_ctrl = wx.TextCtrl( self.setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.email_ctrl, 0, wx.ALL, 5 )

		self.tel = wx.StaticText( self.setting_panel, wx.ID_ANY, self.customString.tel, wx.DefaultPosition, wx.DefaultSize, 0 )
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

		self.save = wx.Button( self.setting_panel, wx.ID_ANY, self.customString.save, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.save, 0, wx.ALL, 5 )

		self.m_button95 = wx.Button( self.setting_panel, wx.ID_ANY, self.customString.cancel, wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.Destroy()

	def onCancel( self, event ):
		self.Destroy()
