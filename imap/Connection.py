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
        print('Connecting to your email IMAP server ({0}).'.format(self.imap_address))
        try:
            self.connection = imapclient.IMAPClient(self.imap_address, ssl=True, ssl_context=self.context)
        except Exception as err:
            print(err)

    def disconnect(self):
        print('')
        print('I am disconnecting you from your email.\n')
        self.connection.logout()

    def login(self):
        print('')
        print('Cool, let\'s login... ')
        try:
            email = input('Email > ')
            password = getpass.getpass('Password > ')
            self.connection.login(email, password)
        except Exception as err:
            print(err)

    def select_folder(self, folder_name):
        print('Selecting Folder: {0}'.format(folder_name))
        self.connection.select_folder(folder_name, readonly=True)

    def list_subjects(self, UIDs):

        rawMessages = self.connection.fetch(UIDs, ['RFC822'])

        # raw messages get returned in a byte format, I need to convert them to strings to parse through them a little bit easier
        print('Converting Raw Messages ...')
        convertedMessages = self.convert(rawMessages);

        print('')
        print(bcolors.OKBLUE + '{:10}{:50}'.format('UID', 'Subject') + bcolors.ENDC)

        subjects = {}
        for uid in convertedMessages:
            parsedMessage = email.message_from_string(convertedMessages[uid]['RFC822'])
            if (uid == 7555):
                print(parsedMessage)
            print('{:10}{:.50}'.format(str(uid), parsedMessage['Subject']))
            subjects[uid] = BeautifulSoup(''.join(str(v) for v in parsedMessage.get_payload()), 'html.parser')

        return subjects

    def convert(self, data):
        if isinstance(data, bytes):  return data.decode('ascii')
        if isinstance(data, dict):   return dict(map(self.convert, data.items()))
        if isinstance(data, tuple):  return map(self.convert, data)
        return data
