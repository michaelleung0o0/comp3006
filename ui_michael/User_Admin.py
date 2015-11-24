import wx
import wx.xrc
import wx.richtext

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