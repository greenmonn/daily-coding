import unittest

from rotate_binary import *

class RotateBinaryTest(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(True, True)

    def test_get_kth_big_element(self):
        self.assertEqual(3, get_kth_big_element([1, 2, 3], 1))
        self.assertEqual(1, get_kth_big_element([1, 2, 3], 3))

    def test_get_generatable_numbers(self):
        pass

    def test_get_