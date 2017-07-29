from imap.Connection import Connection
from datetime import date, timedelta

class Outlook(Connection):

    def __init__(self):
        Connection.__init__(self, 'o365mail.homedepot.com')

    def collect_emails(self):
        print('Searching your outlook folder...')
        UIDs = self.connection.search(['SINCE', date.today()])
        emails = self.fetch_emails_by_uid(UIDs)
        self.list_subjects(emails)

    def collect_emails_by_uid(self, uid):
        print('Search your oulook folder for email {}'.format(uid))
        emails = self.fetch_emails_by_uid([uid])
        print(emails)
