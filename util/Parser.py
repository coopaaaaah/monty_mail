
import argparse

class Parser:
    def __init__(self):
        pass

    def initilaize_arg_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-e", "--email", help="provide email client", choices=['gmail', 'outlook'], default='gmail')
        parser.add_argument("-i", "--uid", help="provide email id", type=int)

        return parser.parse_args()
