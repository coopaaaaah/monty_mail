#! /usr/local/bin/python3

from pick import pick
from imap.Gmail import Gmail
from imap.Outlook import Outlook

def logo():
    print(' _  _ ____ __ _ ___ _ _   _  _ ____ _ _  ')
    print(' |\/| [__] | \|  |   Y    |\/| |--| | |__ ')
    print('')

def main():

    try:
        title = 'Please choose your email client: '
        options = ['1. GMAIL', '2. OUTLOOK']
        choice = int(input('\n'.join(options) + '\nSelect an option: '))

        if (choice != 1 and choice != 2):
            raise Exception('Please select option 1 or 2')

        if (choice == 1):
            connection = Gmail()
            connection.connect()
            connection.login()
            connection.select_folder('INBOX')
            connection.collect_emails()
            connection.disconnect()

        elif (choice == 2):
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
