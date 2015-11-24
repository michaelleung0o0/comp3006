import wx
import wx.xrc
import wx.richtext

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