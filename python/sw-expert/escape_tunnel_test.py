import unittest
from escape_tunnel import *

tunnel_map = [[0, 0, 5, 3, 6, 0],
              [0, 0, 2, 0, 2, 0],
              [3, 3, 1, 3, 7, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]


class EscapeTunnelTest(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(True, True)

    def test_get_next_positions(self):
        self.assertEqual([(2, 0), (2, 2)], get_next_positions((2, 1), tunnel_map, 5, 6, []))

    def test_get_criminal_positions(self):
        self.assertEqual([(2, 1)], get_criminal_positions((2, 1), 0, tunnel_map, 5, 6))
        self.assertEqual(10, len(get_criminal_positions((2, 1), 6, tunnel_map, 5, 6)))
