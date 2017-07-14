class GmailConnection(Connection):

    def __init__(self):
        Connection.__init__(self, 'imap.gmail.com')

    def collect_emails(self):
        UIDs = self.connection.gmail_search(['is:unread in:inbox']) // gmail
        self.list_subjects(UIDs)
