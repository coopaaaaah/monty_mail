#! /usr/local/bin/python3

import sys
from pick import pick
from imap.Gmail import Gmail
from imap.Outlook import Outlook

def logo():
    print(' _  _ ____ __ _ ___ _ _   _  _ ____ _ _  ')
    print(' |\/| [__] | \|  |   Y    |\/| |--| | |__ ')
    print('')

def main():

    arguments = sys.argv[1:]

    try:
        choice = arguments[0]

        if (choice != 'outlook' and choice != 'gmail'):
            raise Exception('\nArgument 1 must be mail client, available mail clients: \n\t-outlook\n\t-gmail')

        if (choice == 'gmail'):
            connection = Gmail()
            connection.connect()
            connection.login()
            connection.select_folder('INBOX')
            connection.collect_emails()
            connection.disconnect()

        elif (choice == 'outlook'):
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
