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
        text1 = ''
        text2 = ''

        with open(name1, 'r') as f:
            text1 = f.read()

        with open(name2, 'r') as f:
            text2 = f.read()

        self.assertEqual(text1, text2)

    def rm_with_opt_args(self, test, namespaces, output):
        rm_file_save(test, namespaces, output=output, style='WebKit', clang_format='clang-format')

    def test_1(self):
        test, expected, output = self.__filenames(1)
        self.rm_with_opt_args(test, ['foo'], output)
        self.assertFilesEqual(expected, output)

    def test_2(self):
        test, expected, output = self.__filenames(2)
        self.rm_with_opt_args(test, ['foo'], output)
        self.assertFilesEqual(expected, output)

    def test_3(self):
        test, expected, output = self.__filenames(3)
        self.rm_with_opt_args(test, ['foo'], output)
        self.assertFilesEqual(expected, output)

    def test_4(self):
        test, expected, output = self.__filenames(4)
        self.rm_with_opt_args(test, ['foo'], output)
        self.assertFilesEqual(expected, output)

    def test_5(self):
        test, expected, output = self.__filenames(5)
        self.rm_with_opt_args(test, ['foo'], output)
        self.assertFilesEqual(expected, output)

    def test_6(self):
        test, expected, output = self.__filenames(6)
        self.rm_with_opt_args(test, ['foo', 'goo'], output)
        self.assertFilesEqual(expected, output)

    def test_7(self):
        test, expected, output = self.__filenames(7)
        self.rm_with_opt_args(test, ['foo', 'goo'], output)
        self.assertFilesEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
