from backports import ssl
from bs4 import BeautifulSoup
import imapclient
import pprint
import getpass
import email

class Connection:

    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_NONE
    context.check_hostname = False
    connection = {}
    imap_address = ''

    def __init__(self, imap_address):
        self.imap_address = imap_address;

    def connect(self):
        try:
            self.connection = imapclient.IMAPClient(self.imap_address, ssl=True, ssl_context=self.context)
        except Exception as err:
            print(err)

    def disconnect(self):
        print('I am disconnecting you from your email.\n')
        self.connection.logout()

    def login(self):
        print('First, we must connect to your email. What is your email address?')
        try:
            email = input('Email > ')
            password = getpass.getpass('Password > ')
            self.connection.login(email, password)
        except Exception as err:
            print(err)
            return 0
        return 1;

    def select_folder(self, folder_name):
        self.connection.select_folder(folder_name, readonly=True)

    def list_subjects(self, UIDs):

        rawMessages = self.connection.fetch(UIDs, ['RFC822'])
        # raw messages get returned in a byte format, I need to convert them to strings to parse through them a little bit easier
        convertedMessages = self.convert(rawMessages);

        print('')
        print(bcolors.OKBLUE + 'UID\tSubject' + bcolors.ENDC)

        subjects = {}
        for uid in convertedMessages:
            parsedMessage = email.message_from_string(convertedMessages[uid]['RFC822'])
            print('{0}\t{1}'.format(uid, parsedMessage['Subject']))
            subjects[uid] = BeautifulSoup(''.join(str(v) for v in parsedMessage.get_payload()), 'html.parser')

        return subjects

    def convert(self, data):
        if isinstance(data, bytes):  return data.decode('ascii')
        if isinstance(data, dict):   return dict(map(self.convert, data.items()))
        if isinstance(data, tuple):  return map(self.convert, data)
        return data

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
