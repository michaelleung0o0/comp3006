"""Subclass of GUI_MainFrame, which is generated by wxFormBuilder."""

import wx
import Stock_Monitor

# Implementing GUI_MainFrame
class SMS( Stock_Monitor.IndexPage ):
	def __init__( self, parent ):
		Stock_Monitor.IndexPage.__init__( self, parent )

	
	# Handlers for GUI_MainFrame events.
	def OnCalculateClick( self, event ):
		# TODO: Implement OnCalculateClick
		pass
	
	def OnExitClick( self, event ):
		# TODO: Implement OnExitClick
                self.Close()