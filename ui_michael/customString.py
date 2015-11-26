class customString:
    def __init__(self, case):
        if case == 'forgetpw':
            self.title = u'Forget Password'
            self.id = u'ID: '
            self.email = u'Email: '
            self.resetpw = u'&Reset Password '
            self.contact = u'&Contect Admin'
            self.cancel = u'&Cancel'
        if case == 'aboutus':
            self.title = u'About Us'
            self.exit = u'&Exit'
            self.content = 'This system is developed by 404 NOT FOUND team from Hong Kong Baptist University.\n404 NOT FOUND:\n12210102 MAK KIT TIN\n15208249 LEUNG KAI HIN'
        if case == 'reg':
            self.title = u'Register'
            self.id = u'ID: '
            self.oldpw = u'Old Password: '
            self.newpw = u'New Password: '
            self.confirmnewpw = u'Confirm New Password: '
            self.email = u'Email: '
            self.tel = u'Telephone: '
            self.save = u'&Save'
            self.cancel = u'&Cancel'
        if case == 'setting':
            self.title = u'Setting'
            self.innertitle = u'System Setting'
            self.arrowchoice1 = u'Positive : Green; Negative : Red'
            self.arrowchoice2 = u'Positive : Red; Negative : Green'
            self.refreshtime = u'Refresh Time'
            self.halfsec = u'0.5 sec'
            self.onesec = u'1 sec'
            self.twosec = u'2 sec'
