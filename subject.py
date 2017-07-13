#! /usr/local/bin/python3

from backports import ssl
import imapclient
import pprint
import getpass
import email

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False

def connect():
    conn = imapclient.IMAPClient("imap.gmail.com", ssl=True, ssl_context=context)
    email = input('Email > ')
    password = getpass.getpass('Password > ')

    conn.login(email, password)
    conn.select_folder('INBOX', readonly=True)
    return conn;

def disconnect(conn):
    print('I am disconnecting you from your email.\n')
    conn.logout();

def search(conn, phrase):
    UIDs = conn.gmail_search(phrase)
    rawMessages = conn.fetch(UIDs, ['RFC822'])

    # raw messages get returned in a byte format, I need to convert them to strings to parse through them a little bit easier
    convertedMessages = convert(rawMessages);

    print('')
    print('UID\tSubject')
    print('')

    for uid in convertedMessages:
        parsedMessage = email.message_from_string(convertedMessages[uid]['RFC822'])
        print('{0}\t{1}'.format(uid, parsedMessage['Subject']))

def convert(data):
    if isinstance(data, bytes):  return data.decode('ascii')
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return map(convert, data)
    return data

class Connection():
    print('')
    print('I am now connecting to your email, David.')
    conn = connect()
    phrase = input('What subject do you want to search for? ')
    if not phrase: 
        phrase = ' '
    search(conn, phrase)
    disconnect(conn);
