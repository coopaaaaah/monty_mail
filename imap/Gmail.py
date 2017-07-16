from imap.Connection import Connection

class Gmail(Connection):

    def __init__(self):
        Connection.__init__(self, 'imap.gmail.com')

    def collect_emails(self):
        print('Searching your Gmail folder ...')
        UIDs = self.connection.gmail_search('is:unread in:inbox')
        self.list_subjects(UIDs)
