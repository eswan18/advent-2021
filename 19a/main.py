from itertools import combinations
from pprint import pprint

from scanner import Scanner


#with open('input.txt', 'rt') as f:
with open('test_input.txt', 'rt') as f:
#with open('test2.txt', 'rt') as f:
    scanner_text = f.read().split('\n\n')

scanners = [Scanner.from_text(s) for s in scanner_text]


for s1, s2 in combinations(scanners, 2):
#    overlap = s1.distance_set & s2.distance_set
#    if len(overlap) >= min_dist_count:
    if s1.overlaps(s2):
        print(f'{s1.number} intersects {s2.number}')
        correspondence = {}
        for c1, d1 in s1.coord_distances.items():
            for c2, d2 in s2.coord_distances.items():
                if len(d1 & d2) >= 11:
                    correspondence[c1] = c2
            # In theory, three should be enough, but not in certain arrangements.
            if len(correspondence) >= 5:
                break
        for c1, c2 in correspondence.items():
            print(f'{c1} in Scanner {s1.number} is the same as {c2} in Scanner {s2.number}')
        break
