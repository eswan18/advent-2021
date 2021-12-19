from dataclasses import dataclass
import re
from typing import Optional, Iterator
from collections import namedtuple

Coord = namedtuple('Coord', 'x,y,z')

SCANNER_PATTERN = re.compile(r'--- scanner (\d+)')

@dataclass
class Scanner:
    number: int
    beacons: list[Coord]
    location: Optional[Coord] = None

    @classmethod
    def from_text(cls, text) -> 'Scanner':
        lines = text.split('\n')
        name_line, *lines = lines
        match = SCANNER_PATTERN.match(name_line)
        number = match.group(1)
        beacons = [
            Coord(*[int(c) for c in line.split(',')])
            for line in lines if len(line) > 0
        ]
        return cls(number, beacons)
    
    def rotated(self, rotation:int = 1) -> 'Scanner':
        '''
        A scanner with the same coords, from the perspective of "up" being N/4 rotations clockwise.
        '''
        if rotation == 1:
            new_beacons = [Coord(-y, x, z) for (x, y, z) in self.beacons]
        elif rotation == 2:
            new_beacons = [Coord(-x, -y, z) for (x, y, z) in self.beacons]
        elif rotation == 3:
            new_beacons = [Coord(y, -x, z) for (x, y, z) in self.beacons]
        else:
            raise ValueError

        return self.__class__(
            number=self.number,
            beacons=new_beacons,
            location=self.location,
        )

    def facing_back(self) -> 'Scanner':
        '''
        A scanner with the same coords, from the perspective of looking backward.
        '''
        new_beacons = [Coord(-x, y, -z) for (x, y, z) in self.beacons]
        return self.__class__(
            number=self.number,
            beacons=new_beacons,
            location=self.location,
        )


    def facing_down(self) -> 'Scanner':
        '''
        A scanner with the same coords, from the perspective of "forward" being N/4 rotations down.
        '''
        new_beacons = [Coord(x, z, -y) for (x, y, z) in self.beacons]
        return self.__class__(
            number=self.number,
            beacons=new_beacons,
            location=self.location,
        )

    def facing_up(self) -> 'Scanner':
        '''
        A scanner with the same coords, from the perspective of "forward" being N/4 rotations up.
        '''
        new_beacons = [Coord(x, -z, y) for (x, y, z) in self.beacons]
        return self.__class__(
            number=self.number,
            beacons=new_beacons,
            location=self.location,
        )

    def facing_right(self) -> 'Scanner':
        '''
        A scanner with the same coords, from the perspective of "forward" being N/4 rotations right.
        '''
        new_beacons = [Coord(-z, y, x) for (x, y, z) in self.beacons]
        return self.__class__(
            number=self.number,
            beacons=new_beacons,
            location=self.location,
        )

    def facing_left(self) -> 'Scanner':
        '''
        A scanner with the same coords, from the perspective of "forward" being N/4 rotations left.
        '''
        new_beacons = [Coord(z, y, -x) for (x, y, z) in self.beacons]
        return self.__class__(
            number=self.number,
            beacons=new_beacons,
            location=self.location,
        )

    def all_rotations(self) -> Iterator['Scanner']:
        facings = (
            self, self.facing_back(),
            self.facing_down(), self.facing_up(),
            self.facing_right(), self.facing_left(),
        )
        for f in facings:
            yield f
            yield f.rotated(1)
            yield f.rotated(2)
            yield f.rotated(3)

    def __iter__(self) -> Iterator[Coord]:
        return iter(self.beacons)

    def __str__(self) -> str:
        s = f'--- scanner {self.number} ---\n'
        for x, y, z in self.beacons:
            s += f'{x},{y},{z}\n'
        return s
