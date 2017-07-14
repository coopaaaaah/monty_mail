#! /usr/local/bin/python3

from imap.Gmail import Gmail
from imap.Outlook import Outlook

def logo():
    print(' _  _ ____ __ _ ___ _ _   _  _ ____ _ _  ')
    print(' |\/| [__] | \|  |   Y    |\/| |--| | |__ ')
    print('')


def main():
    logo()

    connection = Gmail()
    connection.connect()
    connection.login()
    connection.select_folder('INBOX')
    connection.collect_emails()
    connection.disconnect()

    connection = Outlook()
    connection.connect()
    connection.login()
    connection.select_folder('Sent Directly To Me')
    connection.collect_emails()
    connection.disconnect()

main()
