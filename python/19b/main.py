from itertools import combinations
from pprint import pprint

from scanner import Scanner, Coord


with open('input.txt', 'rt') as f:
    scanner_text = f.read().split('\n\n')

scanners = [Scanner.from_text(s) for s in scanner_text]

def merge(scanners: list[Scanner]) -> list[Scanner]:
    '''
    Merge two scanners in a list of them.
    '''
    # Make a copy to avoid weirdness.
    scanners = list(scanners)
    s1 = scanners[0]
    for s2 in scanners[1:]:
        if s1.overlaps(s2):
            print(f'Merging scanners {s1.number} and {s2.number}')
            # This forces everything to stay on the coordinate system of Scanner 0.
            new_s = s1 + s2
            # Remove s1 and s2 from the list.
            scanners = [s for s in scanners if s not in (s1, s2)]
            scanners = [new_s] + scanners
            return scanners

while len(scanners) > 1:
    scanners = merge(scanners)

final_scanner = scanners[0]

manhattan_winner = 0
for b1, b2 in combinations(final_scanner.absorbed, 2):
    x1, y1, z1 = b1
    x2, y2, z2 = b2
    manhattan = sum(abs(i) for i in (x2-x1, y2-y1, z2-z1))
    manhattan_winner = max(manhattan, manhattan_winner)

print(manhattan_winner)
