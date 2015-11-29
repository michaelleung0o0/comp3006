import wx
import wx.xrc
import wx.richtext
import sys
from customString import customString
from apiRequest import apiRequest
import time

###########################################################################
## Class Monitoring_stock
###########################################################################

class Monitoring_stock ( wx.Panel ):

	def __init__( self, parent ):
		self.customString = customString('monitor')

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
		self.englishName = '{:^58}'.format(self.aRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.aRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.aRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.aRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.aRequest.GetLowPrice(self))
		self.change = self.aRequest.GetChange(self)
		self.pctchange = self.aRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay



                self.bRequest = apiRequest(self, '00003')
                self.englishName = '{:^58}'.format(self.bRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.bRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.bRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.bRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.bRequest.GetLowPrice(self))
		self.change = self.bRequest.GetChange(self)
		self.pctchange = self.bRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'

		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay


                self.cRequest = apiRequest(self, '00005')
                self.englishName = '{:^58}'.format(self.cRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.cRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.cRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.cRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.cRequest.GetLowPrice(self))
		self.change = self.cRequest.GetChange(self)
		self.pctchange = self.cRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'

		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay


                self.dRequest = apiRequest(self, '00016')
                self.englishName = '{:^58}'.format(self.dRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.dRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.dRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.dRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.dRequest.GetLowPrice(self))
		self.change = self.dRequest.GetChange(self)
		self.pctchange = self.dRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay

                self.eRequest = apiRequest(self, '00023')
                self.englishName = '{:^58}'.format(self.eRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.eRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.eRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.eRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.eRequest.GetLowPrice(self))
		self.change = self.eRequest.GetChange(self)
		self.pctchange = self.eRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay


                self.fRequest = apiRequest(self, '00066')
                self.englishName = '{:^58}'.format(self.fRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.fRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.fRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.fRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.fRequest.GetLowPrice(self))
		self.change = self.fRequest.GetChange(self)
		self.pctchange = self.fRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay




                self.gRequest = apiRequest(self, '00268')
                self.englishName = '{:^58}'.format(self.gRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.gRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.gRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.gRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.gRequest.GetLowPrice(self))
		self.change = self.gRequest.GetChange(self)
		self.pctchange = self.gRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay




                self.hRequest = apiRequest(self, '00354')
                self.englishName = '{:^58}'.format(self.hRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.hRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.hRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.hRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.hRequest.GetLowPrice(self))
		self.change = self.hRequest.GetChange(self)
		self.pctchange = self.hRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay

                self.iRequest = apiRequest(self, '00388')
                self.englishName = '{:^58}'.format(self.iRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.iRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.iRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.iRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.iRequest.GetLowPrice(self))
		self.change = self.iRequest.GetChange(self)
		self.pctchange = self.iRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay


                self.jRequest = apiRequest(self, '00806')
                self.englishName = '{:^58}'.format(self.jRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.jRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.jRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.jRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.jRequest.GetLowPrice(self))
		self.change = self.jRequest.GetChange(self)
		self.pctchange = self.jRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay






                self.kRequest = apiRequest(self, '00823')
                self.englishName = '{:^58}'.format(self.kRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.kRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.kRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.kRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.kRequest.GetLowPrice(self))
		self.change = self.kRequest.GetChange(self)
		self.pctchange = self.kRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay





                self.lRequest = apiRequest(self, '00857')
                self.englishName = '{:^58}'.format(self.lRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.lRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.lRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.lRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.lRequest.GetLowPrice(self))
		self.change = self.lRequest.GetChange(self)
		self.pctchange = self.lRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay





                self.mRequest = apiRequest(self, '00939')
                self.englishName = '{:^58}'.format(self.mRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.mRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.mRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.mRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.mRequest.GetLowPrice(self))
		self.change = self.mRequest.GetChange(self)
		self.pctchange = self.mRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay





                self.nRequest = apiRequest(self, '01398')
                self.englishName = '{:^58}'.format(self.nRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.nRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.nRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.nRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.nRequest.GetLowPrice(self))
		self.change = self.nRequest.GetChange(self)
		self.pctchange = self.nRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay






                self.oRequest = apiRequest(self, '02388')
                self.englishName = '{:^58}'.format(self.oRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.oRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.oRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.oRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.oRequest.GetLowPrice(self))
		self.change = self.oRequest.GetChange(self)
		self.pctchange = self.oRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay








                self.pRequest = apiRequest(self, '02800')
                self.englishName = '{:^58}'.format(self.pRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.pRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.pRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.pRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.pRequest.GetLowPrice(self))
		self.change = self.pRequest.GetChange(self)
		self.pctchange = self.pRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay





                self.qRequest = apiRequest(self, '02888')
                self.englishName = '{:^58}'.format(self.qRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.qRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.qRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.qRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.qRequest.GetLowPrice(self))
		self.change = self.qRequest.GetChange(self)
		self.pctchange = self.qRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay



                self.rRequest = apiRequest(self, '03328')
                self.englishName = '{:^58}'.format(self.rRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.rRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.rRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.rRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.rRequest.GetLowPrice(self))
		self.change = self.rRequest.GetChange(self)
		self.pctchange = self.rRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay


                self.sRequest = apiRequest(self, '03888')
                self.englishName = '{:^58}'.format(self.sRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.sRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.sRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.sRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.sRequest.GetLowPrice(self))
		self.change = self.sRequest.GetChange(self)
		self.pctchange = self.sRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay


                self.tRequest = apiRequest(self, '03988')
                self.englishName = '{:^58}'.format(self.tRequest.GetEnglishName(self))
		self.currentPrice = 'Price: ' + '{:^11}'.format(self.tRequest.GetCurrentPrice(self))
		self.prefixPrice = 'LDay Price: ' + '{:^11}'.format(self.tRequest.GetPrefixPrice(self))
		self.highPrice = 'High: ' + '{:^11}'.format(self.tRequest.GetHighPrice(self))
		self.lowPrice = 'Low: ' + '{:^11}'.format(self.tRequest.GetLowPrice(self))
		self.change = self.tRequest.GetChange(self)
		self.pctchange = self.tRequest.GetPctChange(self)
                self.changedisplay = '{:^20}'.format(self.change + ' (' + self.pctchange + ')')
		self.changedisplay = 'Chg: ' + self.changedisplay + '\n'
		searchResult = searchResult + self.englishName + "  |  " + self.currentPrice + "  |  " + self.prefixPrice + "  |  " + self.highPrice + "  |  " + self.lowPrice + "  |  " + self.changedisplay
                print ('aaaa')















		# print searchResult
		self.displaySearchResult.Clear()
		self.displaySearchResult.AppendText(searchResult)






	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onEnter( self, event ):
		event.Skip()


	def onSearch( self, event ):
		event.Skip()



