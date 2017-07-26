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
    args = parser.parse_args()

    try:
        if (args.email == 'gmail'):
            connection = Gmail()
            connection.connect()
            connection.login()
            connection.select_folder('INBOX')
            connection.collect_emails()
            connection.disconnect()

        elif (args.email == 'outlook'):
            connection = Outlook()
            connection.connect()
            connection.login()
            connection.select_folder('Sent Directly To Me')
            connection.collect_emails()
            connection.disconnect()
    except KeyboardInterrupt as err:
        print('')
        print('Exiting monty mail.')
    except Exception as err:
        print(err)

main()
