__author__ = 'Amit Botzer'

import json

import os

current_dir = os.path.dirname(__file__)
CONFIGURATION_FILE_PATH = os.path.join(current_dir, 'configuration.ini')


class ConfigurationAdapter(object):

    def __init__(self):
        with open(CONFIGURATION_FILE_PATH, 'r') as configuration_file:
            self.configuration = json.load(configuration_file)

    def get_by_key(self, configuration_key):
        return self.configuration[configuration_key]

#
# configuration = {'CHAT_FILE_PATH':'C:\\Users\\amitb_000\\PycharmProjects\\chat_analyzer\\chat_analyzer\\parser\\chat'}
# with open(CONFIGURATION_FILE_PATH, 'w') as configuration_file:
#     json.dump(configuration, configuration_file)