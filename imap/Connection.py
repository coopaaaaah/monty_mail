from util.bcolors import bcolors
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
        print('')
        try:
            self.connection = imapclient.IMAPClient(self.imap_address, ssl=True, ssl_context=self.context)
        except Exception as err:
            print(err)
        print('Connected to your email IMAP server ({0}).'.format(self.imap_address))

    def disconnect(self):
        print('')
        print('Logging out.\n')
        self.connection.logout()

    def login(self):
        print('')
        print('Let\'s login... ')
        try:
            email = input('Email > ')
            password = getpass.getpass('Password > ')
            self.connection.login(email, password)
        except Exception as err:
            print(err)
            exit(1)
        print('You\'re connected successfully.')

    def select_folder(self, folder_name):
        print('')
        try:
            self.connection.select_folder(folder_name, readonly=True)
        except Exception as err:
            print(err)
            exit(1)
        print('Selected Folder: {0}'.format(folder_name))

    def fetch_emails_by_uid(self, UIDs):
        rawMessages = self.connection.fetch(UIDs, ['RFC822'])
        # raw messages get returned in a byte format, I need to convert them to strings to parse through them a little bit easier
        print('')
        print('Converting Raw Messages ...')
        return self.convert(rawMessages);

    def list_subjects(self, convertedMessages):
        print('Found {0} Messages\n'.format(len(convertedMessages)))
        print(bcolors.OKBLUE + '{:10}{:50}'.format('UID', 'Subject') + bcolors.ENDC)

        for uid in convertedMessages:
            parsedMessage = email.message_from_string(convertedMessages[uid]['RFC822'])
            print('{:10}{:.30s}...'.format(str(uid), parsedMessage['Subject']))
            # BeautifulSoup(''.join(str(v) for v in parsedMessage.get_payload()), 'html.parser')


    def convert(self, data):
        if isinstance(data, bytes):  return data.decode('ascii')
        if isinstance(data, dict):   return dict(map(self.convert, data.items()))
        if isinstance(data, tuple):  return map(self.convert, data)
        return data
