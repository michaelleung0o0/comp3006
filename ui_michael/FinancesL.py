import wx
import wx.xrc
import wx.richtext
import sys

#from Login import Login
from customString import customString
from readNews import readNews
# from apiRequest import apiRequest
###########################################################################
## Class Finances
###########################################################################

class FinancesL ( wx.Panel ):

	def __init__( self, parent ):
		self.customString = customString('finl')
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.TAB_TRAVERSAL )

		self.SetMinSize( wx.Size( 900,600 ) )

		bSizerFrame = wx.BoxSizer( wx.VERTICAL )

		self.f_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		try:
			image_file = 'bg.jpg'
			bmp = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			self.bitmap = wx.StaticBitmap(self.f_panel, -1, bmp, (0,0))
		except IOError:
			raise SystemExit

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self.f_panel, wx.ID_ANY, self.customString.title, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )

		bSizer2.Add( self.title, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer3.SetMinSize( wx.Size( -1,400 ) )
		self.main_c = wx.richtext.RichTextCtrl( self.f_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer3.Add( self.main_c, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.Exit = wx.Button( self.f_panel, wx.ID_ANY, self.customString.exit, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Exit, 0, wx.ALL, 5 )

		self.Back = wx.Button( self.f_panel, wx.ID_ANY, self.customString.logout, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.Back, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 0, 0, 5 )


		self.f_panel.SetSizer( bSizer1 )
		self.f_panel.Layout()
		bSizer1.Fit( self.f_panel )
		bSizerFrame.Add( self.f_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizerFrame )
		self.Layout()

		# Connect Events
		self.Exit.Bind( wx.EVT_BUTTON, self.ExitOnButtonClick )
		self.Back.Bind( wx.EVT_BUTTON, self.onBack )

		self.readNews = readNews(self)
		self.readNews.RSSReader()
		# self.apiRequest = apiRequest(self)
	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ExitOnButtonClick( self, event ):
		sys.exit(0)
	
	def onBack( self, event ):
		self.Destroy()