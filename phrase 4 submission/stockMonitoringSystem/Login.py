import wx
import wx.xrc
import wx.richtext
import sys
from SQLOp import sqlConnection

from Welcome import Welcome
from Register import Register
from Forget_password import Forget_password
from Setting import Setting
from Finances import Finances
from About_Us import About_Us

from customString import customString

###########################################################################
## Class Login
###########################################################################

class Login ( wx.Panel ):

	def __init__( self, parent ):
		self.customString = customString('login')

		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,600 ), style = wx.TAB_TRAVERSAL )

		self.SetMinSize( wx.Size( 900,600 ) )

		bSizerFrame = wx.BoxSizer( wx.VERTICAL )

		self.lg_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.lg_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )




		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.lg_panel, wx.ID_ANY, self.customString.title, wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 36, 74, 90, 92, False, "Arial" ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )


		bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		fgSizer181 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer181.SetFlexibleDirection( wx.BOTH )
		fgSizer181.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText51 = wx.StaticText( self.lg_panel, wx.ID_ANY, self.customString.id, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer181.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_textCtrl31 = wx.TextCtrl( self.lg_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl31.SetMinSize( wx.Size( 250,-1 ) )

		fgSizer181.Add( self.m_textCtrl31, 0, wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( self.lg_panel, wx.ID_ANY, self.customString.pw, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		fgSizer181.Add( self.m_staticText61, 0, wx.ALL, 5 )

		self.m_textCtrl41 = wx.TextCtrl( self.lg_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl41.SetMinSize( wx.Size( 250,-1 ) )

		fgSizer181.Add( self.m_textCtrl41, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( fgSizer181, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( bSizer4, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.login = wx.Button( self.lg_panel, wx.ID_ANY, self.customString.login, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.login, 0, wx.ALL, 5 )

		self.register = wx.Button( self.lg_panel, wx.ID_ANY, self.customString.reg, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.register, 0, wx.ALL, 5 )

		self.forgetPassword = wx.Button( self.lg_panel, wx.ID_ANY, self.customString.forgetpw, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.forgetPassword, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.Exit = wx.Button( self.lg_panel, wx.ID_ANY, self.customString.exit, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.Exit, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer7, 1, 0, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.Setting = wx.Button( self.lg_panel, wx.ID_ANY, self.customString.setting, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.Setting, 0, wx.ALL, 5 )

		self.About_Us = wx.Button( self.lg_panel, wx.ID_ANY, self.customString.about, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.About_Us, 0, wx.ALL, 5 )

		self.News = wx.Button( self.lg_panel, wx.ID_ANY, self.customString.news, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.News, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer8, 0, wx.EXPAND, 5 )


		bSizer1.Add( bSizer6, 0, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		self.lg_panel.SetSizer( bSizer1 )
		self.lg_panel.Layout()
		bSizer1.Fit( self.lg_panel )
		bSizerFrame.Add( self.lg_panel, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerFrame )
		self.Layout()

		# Connect Events
		self.login.Bind( wx.EVT_BUTTON, self.onlogin )
		self.register.Bind( wx.EVT_BUTTON, self.onRegister )
		self.forgetPassword.Bind( wx.EVT_BUTTON, self.onForgetPassword )
		self.Exit.Bind( wx.EVT_BUTTON, self.onExit )
		self.Setting.Bind( wx.EVT_BUTTON, self.onSetting )
		self.About_Us.Bind( wx.EVT_BUTTON, self.onAboutUs )
		self.News.Bind( wx.EVT_BUTTON, self.onNews )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onlogin( self, event ):
		# certifcate
		# sc = sqlConnection("http://localhost", "admin1", "123456", "sms")
		# sc.runSQL("select uid from userinfo")
		# s = sc.printSQLResult("select password from userinfo where username = " + self.m_textCtrl31.GetValue() )
		# # sc.runSQL("select * from userinfo where username = " + self.m_textCtrl31.GetValue() + )
		# if(s == self.m_textCtrl41.GetValue()):
			self.Close()
			self.Hide()

		# print self.m_textCtrl31.GetValue()
		# print self.m_textCtrl41.GetValue()
		# self.Close()
		# self.Hide()

		# Welcome.Show()


	def onRegister( self, event ):
		self.Register = Register(self)
		self.Register.Show()

	def onForgetPassword( self, event ):
		self.Forget_password = Forget_password(self)
		self.Forget_password.Show()

	def onExit( self, event ):
		sys.exit(0)

	def onSetting( self, event ):
		self.Setting = Setting(self)
		self.Setting.Show()

	def onAboutUs( self, event ):
		self.About_Us = About_Us(self)
		self.About_Us.Show()
	def onNews( self, event ):
		self.Close()
		self.finances = Finances(self)
		self.finances.Show()
		# self.FinancesL = FinancesL(self)
		# self.FinancesL.Show()
		# Finances_L.Show()
