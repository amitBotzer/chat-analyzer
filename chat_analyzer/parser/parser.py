# -*- coding: utf-8 -*-

__author__ = 'Amit Botzer'

import codecs
from chat_analyzer.conversation import *
from chat_analyzer.message import *
from chat_analyzer.configuration.configuration_adapter import *

CHAT_FILE_PATH_KEY = 'CHAT_FILE_PATH'


def parse():
    configuration = ConfigurationAdapter()
    chat_file_path = configuration.get_by_key(CHAT_FILE_PATH_KEY)
    messages = []
    with open(chat_file_path, 'r') as chat_file:
        lines = chat_file.readlines()
        for line in lines:
            try:
                line = line.decode("utf8")
                message = parse_message(line)
                messages.append(message)
            except Exception:
                continue
    participants = list(set([message.sender for message in messages]))
    return Conversation(messages, participants)


# message line format:
# 5.8.2015, 19:57 - חיים של ברווז: בדיוק הולכת להתקלח
def parse_message(line):
    if not validate_line(line):
        raise Exception
    try:
        date = get_date_string(line)
        hour = get_hour_string(line)
        sender = get_sender_string(line)
        text = get_text_string(line)
        return Message(date, hour, sender, text)
    except Exception:
        print unicode(line).encode('utf8')
        raise Exception


def validate_line(line):
    if '-' not in line:
        return False
    return True


def get_date_string(line):
    return line.split(',')[0]


def get_hour_string(line):
    return line.split(',')[1].split('-')[0].strip()


def get_sender_string(line):
    return line.split('-')[1].split(':')[0].strip()


def get_text_string(line):
    return line.split('-')[1].split(':')[1].strip()