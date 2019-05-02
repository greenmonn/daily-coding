from escape_beads import *
import unittest

env_1 = [['#', '#', '#', '#'],
         ['#', 'B', '.', '#'],
         ['#', 'R', '0', '#'],
         ['#', '#', '#', '#']]

env_2 = [['#', '#', '#', '#'],
         ['#', 'B', '.', '#'],
         ['#', '.', '.', '#'],
         ['#', 'R', '0', '#'],
         ['#', '#', '#', '#']]

env_3 = [['#', '#', '#', '#'],
         ['#', '.', '.', '#'],
         ['#', '#', '0', '#'],
         ['#', 'R', '.', '#'],
         ['#', '#', '#', '#']]


class TestEscapeBeads(unittest.TestCase):
    def test_count_until_escape(self):
        self.assertEqual(1, count_until_escape(env_1, (2, 1), (2, 2)))
        self.assertEqual(1, count_until_escape(env_2, (3, 1), (3, 2)))
        self.assertEqual(2, count_until_escape(env_3, (3, 1), (2, 2)))

    def test_go_next_pos(self):
        self.assertEqual((2, 1), go_next_pos((-1, 0), (2, 1), env_1))
        self.assertEqual((2, 1), go_next_pos((-1, 0), (3, 1), env_2))
        self.assertEqual((3, 2), go_next_pos((0, 1), (3, 1), env_2))
        self.assertEqual((3, 1), go_next_pos((0, -1), (3, 1), env_2))
        self.assertEqual((3, 1), go_next_pos((1, 0), (3, 1), env_2))


if __name__ == "__main__":
    unittest.main()
