import wx
import wx.xrc
import wx.richtext
import sys
from customString import customString
from apiRequest import apiRequest

###########################################################################
## Class Monitoring_stock
###########################################################################

class Monitoring_stock ( wx.Panel ):

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

                
                self.aRequest = apiRequest(self, '00001')
		self.englishName = '{:>58}'.format(self.aRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.aRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.aRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.aRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.aRequest.GetLowPrice(self))
		self.change = self.aRequest.GetChange(self)
		self.pctchange = self.aRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'
		searchResult = self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay



                self.bRequest = apiRequest(self, '00003')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'

		               
                self.cRequest = apiRequest(self, '00005')
                self.englishName = '{:>58}'.format(self.cRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.cRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.cRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.cRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.cRequest.GetLowPrice(self))
		self.change = self.cRequest.GetChange(self)
		self.pctchange = self.cRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'


                
                self.dRequest = apiRequest(self, '00016')
                self.englishName = '{:>58}'.format(self.dRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.dRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.dRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.dRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.dRequest.GetLowPrice(self))
		self.change = self.dRequest.GetChange(self)
		self.pctchange = self.dRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'

		
                self.eRequest = apiRequest(self, '00023')
                self.englishName = '{:>58}'.format(self.eRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.eRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.eRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.eRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.eRequest.GetLowPrice(self))
		self.change = self.eRequest.GetChange(self)
		self.pctchange = self.eRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'

		
                self.fRequest = apiRequest(self, '00066')
                self.englishName = '{:>58}'.format(self.fRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.fRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.fRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.fRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.fRequest.GetLowPrice(self))
		self.change = self.fRequest.GetChange(self)
		self.pctchange = self.fRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'




                self.gRequest = apiRequest(self, '00268')
                self.englishName = '{:>58}'.format(self.gRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.gRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.gRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.gRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.gRequest.GetLowPrice(self))
		self.change = self.gRequest.GetChange(self)
		self.pctchange = self.gRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'



		
                self.hRequest = apiRequest(self, '00354')
                self.englishName = '{:>58}'.format(self.hRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.hRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'

                self.iRequest = apiRequest(self, '00388')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'

                
                self.jRequest = apiRequest(self, '00806')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'





		
                self.kRequest = apiRequest(self, '00823')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'




		
                self.lRequest = apiRequest(self, '00857')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'




		
                self.mRequest = apiRequest(self, '00939')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'




		
                self.nRequest = apiRequest(self, '01398')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'





                
                self.oRequest = apiRequest(self, '02388')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'







		
                self.pRequest = apiRequest(self, '02800')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'




		
                self.qRequest = apiRequest(self, '02888')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'


		
                self.rRequest = apiRequest(self, '03328')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'

		
                self.sRequest = apiRequest(self, '03888')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'

		
                self.tRequest = apiRequest(self, '03988')
                self.englishName = '{:>58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:>13}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:>13}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:>13}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:>13}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:>24}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay '\n'













		
		# print searchResult
		self.displaySearchResult.Clear()
		self.displaySearchResult.AppendText(searchResult)



		


	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onEnter( self, event ):
		event.Skip()

		
	def onSearch( self, event ):
		# print self.search_box.GetValue()
		#code = str(self.search_box.GetValue())
		self.aRequest = apiRequest(self, code)
		self.englishName = 'Name: ' + self.aRequest.GetEnglishName(self)
		self.currentPrice = 'Current Price: ' + self.aRequest.GetCurrentPrice(self)
		self.prefixPrice = 'Yesterday Price: ' + self.aRequest.GetPrefixPrice(self)
		self.highPrice = 'Today High Price: ' + self.aRequest.GetHighPrice(self)
		self.lowPrice = 'Today Low Price: ' + self.aRequest.GetLowPrice(self)
		self.change = 'Price Change: ' + self.aRequest.GetChange(self)
		self.pctchange = 'Name: ' + self.aRequest.GetPctChange(self)

                searchResult = self.englishName + "   |   " + self.currentPrice + "   |   " + self.prefixPrice + "   |   " + self.highPrice + "   |   " + self.lowPrice + "   |   " + self.change + " (" + self.pctchange + ")"

		# print searchResult
		self.displaySearchResult.Clear()
		self.displaySearchResult.AppendText(searchResult)
		# print searchResult
		# self.aRequest.UpdateSearchCode(event, code)

                


