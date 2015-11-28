import wx
import wx.xrc
import wx.richtext
import sys
from customString import customString
from apiRequest import apiRequest

###########################################################################
## Class Search_Stock
###########################################################################

class Search_Stock ( wx.Panel ):

	def __init__( self, parent ):
		self.customString = customString('search')

		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,570 ), style = wx.TAB_TRAVERSAL )

		self.SetMinSize( wx.Size( 900,600 ) )

		bSizerFrame = wx.BoxSizer( wx.VERTICAL )

		self.s_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.title = wx.StaticText( self.s_panel, wx.ID_ANY, self.customString.title, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )

		bSizer2.Add( self.title, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer3.SetMinSize( wx.Size( -1,400 ) )
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.search_tit = wx.StaticText( self.s_panel, wx.ID_ANY, self.customString.searchsk, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_tit.Wrap( -1 )
		bSizer4.Add( self.search_tit, 0, wx.ALL, 5 )

		self.search_box = wx.SearchCtrl( self.s_panel, wx.ID_ANY, self.customString.searchdef, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_box.ShowSearchButton( True )
		self.search_box.ShowCancelButton( True )
		bSizer4.Add( self.search_box, 1, wx.ALL, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.DisplaySearchResult = wx.Panel( self.s_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.DisplaySearchResult.Enable( False )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		# searchResult = self.englishName + "\n" + self.currentPrice + "\n" + self.prefixPrice + "\n" + self.highPrice + "\n" + self.lowPrice + "\n" + self.change + " (" + self.pctchange + ")"

		self.displaySearchResult = wx.richtext.RichTextCtrl( self.DisplaySearchResult, wx.ID_ANY, '', wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.displaySearchResult.SetMinSize( wx.Size( -1,700 ) )

		bSizer6.Add( self.displaySearchResult, 1, wx.EXPAND |wx.ALL, 5 )


		self.DisplaySearchResult.SetSizer( bSizer6 )
		self.DisplaySearchResult.Layout()
		bSizer6.Fit( self.DisplaySearchResult )
		bSizer5.Add( self.DisplaySearchResult, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer1.Add( bSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.s_panel.SetSizer( bSizer1 )
		self.s_panel.Layout()
		bSizer1.Fit( self.s_panel )
		bSizerFrame.Add( self.s_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizerFrame )
		self.Layout()

		# Connect Events
		self.search_box.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.onSearch )
		self.search_box.Bind( wx.EVT_TEXT_ENTER, self.onSearch )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onSearch( self, event ):
		# print self.search_box.GetValue()
		code = str(self.search_box.GetValue())
		self.aRequest = apiRequest(self, code)
		self.englishName = 'Name: ' + self.aRequest.GetEnglishName(self)
		self.currentPrice = 'Current Price: ' + self.aRequest.GetCurrentPrice(self)
		self.prefixPrice = 'Yesterday Price: ' + self.aRequest.GetPrefixPrice(self)
		self.highPrice = 'Today High Price: ' + self.aRequest.GetHighPrice(self)
		self.lowPrice = 'Today Low Price: ' + self.aRequest.GetLowPrice(self)
		self.change = 'Price Change: ' + self.aRequest.GetChange(self)
		self.pctchange = 'Name: ' + self.aRequest.GetPctChange(self)

		searchResult = self.englishName + "\n" + self.currentPrice + "\n" + self.prefixPrice + "\n" + self.highPrice + "\n" + self.lowPrice + "\n" + self.change + " (" + self.pctchange + ")"
		# print searchResult
		self.displaySearchResult.Clear()
		self.displaySearchResult.AppendText(searchResult)
		# print searchResult
		# self.aRequest.UpdateSearchCode(event, code)
