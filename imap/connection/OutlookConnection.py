class OutlookConnection(Connection):

    def __init__(self):
        Connection.__init__(self, 'o365mail.homedepot.com')

    def collect_emails(self):
        UIDs = self.connection.search([u'UNSEEN']) // outlook
        self.list_subjects(UIDs)
