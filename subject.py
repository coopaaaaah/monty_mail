#! /usr/local/bin/python3

from backports import ssl
from bs4 import BeautifulSoup
import imapclient
import pprint
import getpass
import email

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def logo():
    print(' _  _ ____ __ _ ___ _ _   _  _ ____ _ _  ')
    print(' |\/| [__] | \|  |   Y    |\/| |--| | |__ ')
    print('')

def select_imap():
    return 'imap.gmail.com'

def connect(address):

    print('First, we must connect to your email. What is your email address?')
    conn = imapclient.IMAPClient(address, ssl=True, ssl_context=context)
    email = input('Email > ')
    password = getpass.getpass('Password > ')

    conn.login(email, password)
    conn.select_folder('INBOX', readonly=True)
    return conn;

def disconnect(conn):
    print('I am disconnecting you from your email.\n')
    conn.logout();

def collect_emails(conn):
    UIDs = conn.gmail_search('is:unread in:inbox')
    rawMessages = conn.fetch(UIDs, ['RFC822'])

    # raw messages get returned in a byte format, I need to convert them to strings to parse through them a little bit easier
    convertedMessages = convert(rawMessages);

    print('')
    print(bcolors.OKBLUE + 'UID\tSubject' + bcolors.ENDC)

    subjects = {}
    for uid in convertedMessages:
        parsedMessage = email.message_from_string(convertedMessages[uid]['RFC822'])
        print('{0}\t{1}'.format(uid, parsedMessage['Subject']))
        subjects[uid] = BeautifulSoup(''.join(str(v) for v in parsedMessage.get_payload()), 'html.parser')

    return subjects

def convert(data):
    if isinstance(data, bytes):  return data.decode('ascii')
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return map(convert, data)
    return data

def main():
    logo()
    imap = select_imap()
    conn = connect(imap)
    emails = collect_emails(conn)

    for key in emails:
        print(emails[key].find(id='UnsubscribeUrl'))

    disconnect(conn);

main()
