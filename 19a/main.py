from itertools import combinations
from pprint import pprint

from scanner import Scanner


with open('input.txt', 'rt') as f:
    scanner_text = f.read().split('\n\n')

scanners = [Scanner.from_text(s) for s in scanner_text]


def merge(scanners: list[Scanner]) -> list[Scanner]:
    '''
    Merge two scanners in a list of them.
    '''
    # Make a copy to avoid weirdness.
    scanners = list(scanners)
    for s1, s2 in combinations(scanners, 2):
        if s1.overlaps(s2):
            print(f'Merging scanners {s1.number} and {s2.number}')
            # This forces everything to stay on the coordinate system of Scanner 0.
            if s1.number < s2.number:
                new_s = s1 + s2
            else:
                new_s = s2 + s1
            # Remove s1 and s2 from the list.
            scanners = [s for s in scanners if s not in (s1, s2)]
            scanners.append(new_s)
            return scanners

while len(scanners) > 1:
    scanners = merge(scanners)

print(len(scanners[0].beacons))
