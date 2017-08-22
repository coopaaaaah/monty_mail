
import configparser
import os.path

class Config:

    def __init__(self):
        self.config_file = os.path.expanduser('~') + '/.monty_mail.ini'
        pass

    def build_default_config(self, config):

        config['DEFAULT'] = {'token': '45123412',
                            'password': '********'}

        with open(self.config_file, 'w') as configfile:
            config.write(configfile)

    def collect_config(self):

        config = configparser.ConfigParser()

        if not os.path.exists(self.config_file):
            self.build_default_config(config)

        return config.read(self.config_file)
