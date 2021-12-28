import sys
import unittest

sys.path.append('.')
from distance import distance

class Test(unittest.TestCase):
    def test_distances(self):
        assert distance('a', 'b') == 1
        assert distance('a', 'k') == 10
        assert distance('c', 'l') == 1
        assert distance('e', 'q') == 2
