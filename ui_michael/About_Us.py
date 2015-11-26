import wx
import wx.xrc
import wx.richtext
import sys
from customString import customString


###########################################################################
## Class About_Us
###########################################################################



class About_Us ( wx.Frame ):

	def __init__( self, parent ):
		self.customString = customString('aboutus')
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = self.customString.title, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText30 = wx.StaticText( self.m_panel11, wx.ID_ANY, self.customString.title, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		self.m_staticText30.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )

		bSizer63.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_richText3 = wx.richtext.RichTextCtrl( self.m_panel11, wx.ID_ANY, self.customString.content, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer63.Add( self.m_richText3, 1, wx.EXPAND |wx.ALL, 5 )

		self.exit = wx.Button( self.m_panel11, wx.ID_ANY, self.customString.exit, wx.DefaultPosition, wx.DefaultSize, 0 )
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
		# event.Skip()
		self.Destroy()
