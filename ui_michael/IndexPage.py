import wx
import wx.xrc
import wx.richtext



###########################################################################
## Index Page
###########################################################################

class IndexPage ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, wx.ID_ANY)
        self.Login_frame_1 = Login_frame_1.__init__( self, parent )
        self.Home_Frame_2 = Home_Frame_2.__init__( self, parent )
        self.News_Frame_3 = News_Frame_3.__init__( self, parent )
        self.Search_stock_Frame_4 = Search_stock_Frame_4.__init__( self, parent )
        self.Monitoring_Frame_5 = Monitoring_Frame_5.__init__( self, parent )
        self.Admin_6 = Admin_6.__init__( self, parent )
        #self.User_Admin = User_Admin (self)
        #self.Statistics = Statistics (self)
        #self.Setting = Setting (self)

        self.Home_Frame_2.Hide()
        self.News_Frame_3.Hide()
        self.Search_stock_Frame_4.Hide()
        self.Monitoring_Frame_5.Hide()
        self.Admin_6.Hide()
        #self.User_Admin.Hide()
        #self.Statistics.Hide()
        #self.Setting.Hide()