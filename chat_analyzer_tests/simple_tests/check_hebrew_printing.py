# -*- coding: utf-8 -*-

__author__ = 'Amit Botzer'

import unittest
import locale

class HebrewTest(unittest.TestCase):

    def test_hebrew_printing(self):
        word = 'שלום'.decode('utf8')
        print(locale.getpreferredencoding())
        print word.encode('utf8')

if __name__ == '__main__':
    unittest.main()