from dataclasses import dataclass
from collections import namedtuple
import re
from typing import Optional

SCANNER_PATTERN = re.compile(r'--- scanner (\d+)')


with open('test_input.txt', 'rt') as f:
    scanner_text = f.read().split('\n\n')

Coord = namedtuple('Coord', 'x,y,z')

@dataclass
class Scanner:
    number: int
    scanners = list[Coord]
    location: Optional[Coord] = None

def parse_scanner(text) -> Scanner:
    lines = text.split('\n')
    name_line, *lines = lines
    match = SCANNER_PATTERN.match(name_line)
    number = match.groups(1)
    scanners = [
        Coord(*[int(c) for c in line.split(',')])
        for line in lines if len(line) > 0
    ]
    return Scanner(number, scanners)

scanners = [parse_scanner(s) for s in scanner_text]
