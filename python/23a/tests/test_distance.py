import sys
import unittest

sys.path.append('.')
from distance import distance, n_away

class Test(unittest.TestCase):
    def test_distances(self):
        assert distance('a', 'b') == 1
        assert distance('a', 'k') == 10
        assert distance('c', 'l') == 1
        assert distance('e', 'q') == 2

    def test_n_away(self):
        assert n_away('p', 1) == {'l'}
        assert n_away('g', 2) == {'i', 'r', 'e'}
        assert n_away('a', 5) == {'m', 'f'}
        assert n_away('d', 7) == {'k', 's'}
