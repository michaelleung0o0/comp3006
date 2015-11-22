#----------------------------------------------------------------------
# A very simple wxPython example.  Just a wx.Frame, wx.Panel,
# wx.StaticText, wx.Button, and a wx.BoxSizer, but it shows the basic
# structure of any wxPython application.
#----------------------------------------------------------------------

import wx
import requests
from urllib2 import Request, urlopen, URLError

mAppName = "Stock Management System";
mUrl = "http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=00001";
mContent ="";

class MyFrame(wx.Frame):
    """
    This is MyFrame.  It just shows a few controls on a wxPanel,
    and has a simple menu.
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title,
                          pos=(150, 150), size=(350, 200))

        # Create the menubar
        menuBar = wx.MenuBar()

        # and a menu
        menu = wx.Menu()

        # add an item to the menu, using \tKeyName automatically
        # creates an accelerator, the third param is some help text
        # that will show up in the statusbar
        menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit this simple sample")

        # bind the menu event to an event handler
        self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)

        # and put the menu on the menubar
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()


        # Now create the Panel to put the other controls on.
        panel = wx.Panel(self)

        # self.CallRequest()

        # and a few controls
        text = wx.StaticText(panel, -1, mContent)
        text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        text.SetSize(text.GetBestSize())
        btn = wx.Button(panel, -1, "Close")
        funbtn = wx.Button(panel, -1, "Just for fun...")
        callbtn = wx.Button(panel, -1, "CallRequest")
        # bind the button events to handlers
        self.Bind(wx.EVT_BUTTON, self.OnTimeToClose, btn)
        self.Bind(wx.EVT_BUTTON, self.OnFunButton, funbtn)
        self.Bind(wx.EVT_BUTTON, self.CallRequest, callbtn)
        # Use a sizer to layout the controls, stacked vertically and with
        # a 10 pixel border around each
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.ALL, 10)
        sizer.Add(btn, 0, wx.ALL, 10)
        sizer.Add(funbtn, 0, wx.ALL, 10)
        sizer.Add(callbtn, 0, wx.ALL, 10)
        panel.SetSizer(sizer)
        panel.Layout()


    def OnTimeToClose(self, evt):
        """Event handler for the button click."""
        print "See ya later!"
        self.Close()

    def OnFunButton(self, evt):
        """Event handler for the button click."""
        print "Having fun yet?"

    def CallRequest(self, evt):
        # r = requests.get( mUrl, auth=('user', 'pass'))
        # r.status_code
        # r.headers['content-type']
        # r.text
        # mContent = r;
        # print "request"
        request = Request(mUrl)

        try:
            response = urlopen(request)
            kittens = response.read()
            print kittens[559:1000]
        except URLError, e:
            print 'No kittez. Got an error code:', e

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, mAppName)
        self.SetTopWindow(frame)

        print "Print statements go to this stdout window by default."

        frame.Show(True)
        return True

app = MyApp(redirect=True)
app.MainLoop()
