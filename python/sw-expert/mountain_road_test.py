import unittest
from mountain_road import *

N = 5
maxCutDepth = 1
map = [[9, 3, 2, 3, 2],
       [6, 3, 1, 7, 5],
       [3, 4, 8, 9, 9],
       [2, 3, 7, 7, 7],
       [7, 6, 5, 5, 8]]

map_2 = [[8, 3, 9, 5],
         [4, 6, 8, 5],
         [8, 1, 5, 1],
         [4, 9, 5, 5]]


class MountainRoadTest(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(True, True)

    def test_build_road_simple(self):
        maxLength = build_road(4, 4, map_2)
        self.assertEqual(4, maxLength)

    def test_build_road_from(self):
        self.assertEqual(4, build_road_from((0, 2), 4, 4, 1, map_2))

    def test_get_highest_points(self):
        self.assertEqual([(0, 2), (3, 1)], get_highest_points(4, map_2))

    def test_build_road_example(self):
        maxLength = build_road(N, maxCutDepth, map)

        self.assertEqual(6, maxLength)
