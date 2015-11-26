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
## Class Forget_password
###########################################################################

class Forget_password ( wx.Frame ):

	def __init__( self, parent ):
                self.customString = customString('forgetpw')
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = self.customString.title, pos = wx.DefaultPosition, size = wx.Size( 500,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 500,200 ), wx.DefaultSize )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		self.f_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self.f_panel, wx.ID_ANY, self.customString.title, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )

		bSizer1.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.id = wx.StaticText( self.f_panel, wx.ID_ANY, self.customString.id, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id.Wrap( -1 )
		fgSizer.Add( self.id, 0, wx.ALL, 5 )

		self.id_box = wx.TextCtrl( self.f_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id_box.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer.Add( self.id_box, 0, wx.ALL, 5 )

		self.email = wx.StaticText( self.f_panel, wx.ID_ANY, self.customString.email, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )
		fgSizer.Add( self.email, 0, wx.ALL, 5 )

		self.email_box = wx.TextCtrl( self.f_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email_box.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer.Add( self.email_box, 0, wx.ALL, 5 )


		bSizer1.Add( fgSizer, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.reset_password = wx.Button( self.f_panel, wx.ID_ANY, self.customString.resetpw, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.reset_password, 0, wx.ALL, 5 )

		self.Contect_Admin = wx.Button( self.f_panel, wx.ID_ANY, self.customString.contact, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.Contect_Admin, 0, wx.ALL, 5 )

		self.cancel = wx.Button( self.f_panel, wx.ID_ANY, self.customString.cancel, wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.Destroy()

	def onContect( self, event ):
		event.Skip()

	def onCancel( self, event ):
		self.Destroy()

