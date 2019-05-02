from problem_title import *
import unittest


class TestTitle(unittest.TestCase):
    def test_number_of_titles(self):
        print(number_of_titles(['A']))
        self.assertEqual(2, number_of_titles(['Air', 'Dad', 'Ear', 'Blue', 'Ace']))

        self.assertEqual(1, number_of_titles(['Snow_White', 'A_Problem', 'Another_Problem']))


if __name__ == '__main__':
    unittest.main()
