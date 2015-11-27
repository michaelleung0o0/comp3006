import wx
import wx.xrc
import wx.richtext
import sys
from customString import customString

from Register import Register
from Forget_password import Forget_password
from Setting import Setting
from FinancesL import FinancesL
from About_Us import About_Us

###########################################################################
## Class Admin
###########################################################################

class Admin ( wx.Panel ):

	def __init__( self, parent ):
		self.customString = customString('admin')
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,570 ), style = wx.TAB_TRAVERSAL )

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

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onSearchID( self, event ):
		event.Skip()

