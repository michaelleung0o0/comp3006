import wx
import SMS

#Auto generate code 
app = wx.App()
main_frm = SMS.SMS(None)
main_frm.Show()
app.MainLoop()