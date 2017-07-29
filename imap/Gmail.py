from imap.Connection import Connection

class Gmail(Connection):

    def __init__(self):
        Connection.__init__(self, 'imap.gmail.com')

    def collect_emails(self):
        print('Searching your Gmail folder ...')
        UIDs = self.connection.gmail_search('is:unread in:inbox')
        emails = self.fetch_emails_by_uid(UIDs)
        self.list_subjects(emails)

    def collect_emails_by_uid(self, uid):
        print('Search your oulook folder for email {}'.format(uid))
        emails = self.fetch_emails_by_uid([uid])
        print(emails)
