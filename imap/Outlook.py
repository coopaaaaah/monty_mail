from imap.Connection import Connection
from datetime import date, timedelta

class Outlook(Connection):

    def __init__(self):
        Connection.__init__(self, 'o365mail.homedepot.com')

    def collect_emails(self):
        print('Searching your outlook folder...')
        print(date.today())
        UIDs = self.connection.search(['SINCE', date.today()])
        self.list_subjects(UIDs)
