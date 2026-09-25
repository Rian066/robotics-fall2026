import os
import unittest
from week03_pattern.pattern import build_pattern

class MyPatternTests(unittest.TestCase):
    def test_geometry(self):
        s = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        self.assertEqual(len(s), 4)
        self.assertTrue(all(x.linear_x == 0.15 for x in s))

    def test_order(self):
        s = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        self.assertEqual([x.angular_z for x in s], [0.5, -0.5, 0.5, -0.5])
