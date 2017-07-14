from imap.Connection import Connection

class Outlook(Connection):

    def __init__(self):
        Connection.__init__(self, 'o365mail.homedepot.com')

    def collect_emails(self):
        UIDs = self.connection.search([u'UNSEEN'])
        self.list_subjects(UIDs)
