# -*- coding: utf-8 -*-

__author__ = 'Amit Botzer'


import unittest
from chat_analyzer.parser.parser import *
from chat_analyzer.message import *

SAMPLE_RAW_MESSAGES = ['9.8.2015, 10:01 - amit botzer: חחח את מפחידה אותי',
                       '9.8.2015, 10:01 - חיים של ברווז: יואו איזה כיף לך בטח אתה עדיין בבית']


class ParserTest(unittest.TestCase):

    def test_parse(self):
        conversation = parse()
        self.assertEqual(2, len(conversation.participants))

    def test_get_date_string(self):
        for SAMPLE_RAW_MESSAGE in SAMPLE_RAW_MESSAGES:
            date = get_date_string(SAMPLE_RAW_MESSAGE)
            self.assertEqual('9.8.2015', date)

    def test_get_date_string(self):
        for SAMPLE_RAW_MESSAGE in SAMPLE_RAW_MESSAGES:
            hour = get_hour_string(SAMPLE_RAW_MESSAGE)
            self.assertEqual('10:01', hour)

    def test_get_sender_string(self):
        sender = get_sender_string(SAMPLE_RAW_MESSAGES[0])
        self.assertEqual('amit botzer', sender)
        sender = get_sender_string(SAMPLE_RAW_MESSAGES[1])
        self.assertEqual('חיים של ברווז', sender)

    def test_get_text_string(self):
        text = get_text_string(SAMPLE_RAW_MESSAGES[0])
        self.assertEqual('חחח את מפחידה אותי', text)
        text = get_text_string(SAMPLE_RAW_MESSAGES[1])
        self.assertEqual('יואו איזה כיף לך בטח אתה עדיין בבית', text)

if __name__ == '__main__':
    unittest.main()