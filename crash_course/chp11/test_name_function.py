# coding: utf-8
import unittest

from crash_course.chp8 import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('fff', 'lll')
        self.assertEqual(formatted_name, 'jjj lll')


unittest
