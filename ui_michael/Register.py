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
## Class Register
###########################################################################

class Register ( wx.Frame ):

	def __init__( self, parent ):
                self.customString = customString('reg')
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,320 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		self.r_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self.r_panel, wx.ID_ANY, self.customString.title, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )

		bSizer2.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer.SetFlexibleDirection( wx.VERTICAL )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.id = wx.StaticText( self.r_panel, wx.ID_ANY, self.customString.id, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id.Wrap( -1 )
		fgSizer.Add( self.id, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.ID_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer.Add( self.ID_ctrl, 1, wx.ALL, 5 )

		self.OLD_Password = wx.StaticText( self.r_panel, wx.ID_ANY, self.customString.oldpw, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OLD_Password.Wrap( -1 )
		fgSizer.Add( self.OLD_Password, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.OPW_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer.Add( self.OPW_ctrl, 1, wx.ALL, 5 )

		self.n_p = wx.StaticText( self.r_panel, wx.ID_ANY, self.customString.newpw, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.n_p.Wrap( -1 )
		fgSizer.Add( self.n_p, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.NPW_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer.Add( self.NPW_ctrl, 0, wx.ALL, 5 )

		self.c_p = wx.StaticText( self.r_panel, wx.ID_ANY, self.customString.confirmnewpw, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_p.Wrap( -1 )
		fgSizer.Add( self.c_p, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.CNPW_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer.Add( self.CNPW_ctrl, 0, wx.ALL, 5 )

		self.email = wx.StaticText( self.r_panel, wx.ID_ANY, self.customString.email, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )
		fgSizer.Add( self.email, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.email_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.email_ctrl, 0, wx.ALL, 5 )

		self.tel = wx.StaticText( self.r_panel, wx.ID_ANY, self.customString.tel, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tel.Wrap( -1 )
		fgSizer.Add( self.tel, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.tel_ctrl = wx.TextCtrl( self.r_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.tel_ctrl, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer86 = wx.BoxSizer( wx.HORIZONTAL )

		self.save = wx.Button( self.r_panel, wx.ID_ANY, self.customString.save, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer86.Add( self.save, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cancel = wx.Button( self.r_panel, wx.ID_ANY, self.customString.cancel, wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.Destroy()

	def onCancel( self, event ):
		self.Destroy()

