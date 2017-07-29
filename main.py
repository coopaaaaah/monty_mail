#! /usr/local/bin/python3

import sys
import argparse
from pick import pick
from imap.Gmail import Gmail
from imap.Outlook import Outlook

def logo():
    print(' _  _ ____ __ _ ___ _ _   _  _ ____ _ _  ')
    print(' |\/| [__] | \|  |   Y    |\/| |--| | |__ ')
    print('')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="provide email client", choices=['gmail', 'outlook'], default='gmail')
    parser.add_argument("-i", "--uid", help="provide email id", type=int)

    args = parser.parse_args()

    try:
        if (args.email == 'gmail'):
            connection = Gmail()
            connection.connect()
            connection.login()
            connection.select_folder('INBOX')
            if (args.uid is None):
                connection.collect_emails()
            else:
                connection.collect_emails_by_uid(args.uid)
            connection.disconnect()

        elif (args.email == 'outlook'):
            connection = Outlook()
            connection.connect()
            connection.login()
            connection.select_folder('Sent Directly To Me')
            if (args.uid is None):
                connection.collect_emails()
            else:
                connection.collect_emails_by_uid(args.uid)
            connection.disconnect()
    except KeyboardInterrupt as err:
        print('')
        print('Exiting monty mail.')
    except Exception as err:
        print(err)

main()
