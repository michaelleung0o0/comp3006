"""Subclass of GUI_MainFrame, which is generated by wxFormBuilder."""

import wx
import loginPage

# Implementing GUI_MainFrame
class SMS( loginPage.Login_frame_1 ):
	# def __init__( self, parent ):
		# Stock_Monitor.Login_frame_1.__init__( self, parent )
	def __init__( self, *args, **kwargs ):
		loginPage.Login_frame_1.__init__( self, *args, **kwargs )


	# Handlers for GUI_MainFrame events.
	def OnCalculateClick( self, event ):
		# TODO: Implement OnCalculateClick
		pass

	def OnExitClick( self, event ):
		# TODO: Implement OnExitClick
                self.Close()
