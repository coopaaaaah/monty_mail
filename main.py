#! /usr/local/bin/python3

from util.Parser import Parser
from util.Config import Config
from imap.Gmail import Gmail
from imap.Outlook import Outlook

def logo():
    print(' _  _ ____ __ _ ___ _ _   _  _ ____ _ _  ')
    print(' |\/| [__] | \|  |   Y    |\/| |--| | |__ ')
    print('')

def main():

    args = Parser().initilaize_arg_parser()
    config = Config().collect_config()

    try:
        if (args.email == 'gmail'):
            connection = Gmail()
            connection.connect()
            connection.login()
            connection.select_folder('INBOX')
            if (args.uid is None):
                connection.collect_emails()
            else:
                connection.collect_emails(args.uid)
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
