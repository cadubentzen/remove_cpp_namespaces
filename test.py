#!/usr/bin/python3

import unittest
import re
from namespace import rm_file_save

class TestNamespaceRemover(unittest.TestCase):
    def __filenames(self, index):
        return ('tests/test%d.cpp' % index,
                'tests/test%d_expected.cpp' % index,
                'tests/test%d_output.cpp' % index)

    def assertFilesEqual(self, name1, name2):
        text1_original = ''
        text2_original = ''

        text1 = ''
        text2 = ''

        with open(name1, 'r') as f:
            text1_original = f.read()
            text1 = text1_original.replace('\n', '')
            text1 = text1.replace(' ', '')

        with open(name2, 'r') as f:
            text2_optional = f.read()
            text2 = text2_original.replace('\n', '')
            text2 = text2.replace(' ', '')

        self.assertEqual(text1, text2)

    def rm_with_opt_args(self, test, namespace, output):
        rm_file_save(test, namespace, output=output, style='WebKit', clang_format='clang-format-6.0')

    def test_1(self):
        test, expected, output = self.__filenames(1)
        self.rm_with_opt_args(test, 'foo', output)
        self.assertFilesEqual(expected, output)

    def test_2(self):
        test, expected, output = self.__filenames(2)
        self.rm_with_opt_args(test, 'foo', output)
        self.assertFilesEqual(expected, output)

    def test_3(self):
        test, expected, output = self.__filenames(3)
        self.rm_with_opt_args(test, 'foo', output)
        self.assertFilesEqual(expected, output)

    def test_4(self):
        test, expected, output = self.__filenames(4)
        self.rm_with_opt_args(test, 'foo', output)
        self.assertFilesEqual(expected, output)

    def test_5(self):
        test, expected, output = self.__filenames(5)
        self.rm_with_opt_args(test, 'foo', output)
        self.assertFilesEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
