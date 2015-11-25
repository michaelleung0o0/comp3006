import wx
import wx.xrc
import wx.richtext
import sys

from Login import Login

class IndexPage ( wx.Frame ):
    def __init__( self, parent ):
		wx.Frame.__init__( self, parent, wx.ID_ANY, size= wx.Size( 900,650 ))
		# global Finances_L
		# Finances_L = Finances_L(self)
		# global Login
		# Login = Login( self )
		# global Welcome
		# Welcome = Welcome( self )
		# global Search_Stock
		# Search_Stock = Search_Stock( self )
		# global Monitoring_stock
		# Monitoring_stock = Monitoring_stock(self)
		# global finances
		# finances = Finances( self )
		# global Admin
		# Admin = Admin( self )

		# Login.__init__('Login', parent)
		# os.system('python Login.py')
		self.l = Login(self)

		# self.child = Login(self)
		# self.child.show()

		# Login.Show()
		# Finances_L.Hide()
		# Welcome.Hide()
		# Search_Stock.Hide()
		# Monitoring_stock.Hide()
		# finances.Hide()
		# Admin.Hide()

	# def callWelcome( self ):
	# 	self.w = Welcome(self)



