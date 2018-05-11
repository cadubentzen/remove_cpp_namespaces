#!/usr/bin/python3

import unittest
from brace import find_matching_brace, get_inner_text

class TestBrace(unittest.TestCase):
    def assertBrace(self, text, index):
        self.assertEqual(find_matching_brace(text), index)

    def assertInnerText(self, text, result):
        self.assertEqual(get_inner_text(text), result)

    def test_simple(self):
        self.assertBrace('{}', 1)

    def test_invalid(self):
        self.assertBrace('{{}', -1)

    def test_two(self):
        self.assertBrace('{{}}', 3)

    def test_letters(self):
        self.assertInnerText('{a{aa}ab}c', 'a{aa}ab')

    def test_letters_before(self):
        self.assertInnerText('x{a{aa}ab}c', 'a{aa}ab')

if __name__ == '__main__':
    unittest.main()
