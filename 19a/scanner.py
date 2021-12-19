from math import sqrt
from dataclasses import dataclass
import re
from functools import cached_property
from itertools import combinations
from typing import Optional, Iterator
from collections import namedtuple, defaultdict

Coord = namedtuple('Coord', 'x,y,z')

SCANNER_PATTERN = re.compile(r'--- scanner (\d+)')
# How many common distances would exist across 12 points.
MIN_OVERLAP = sum(range(12))

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
    
    def offset(self, x: int = 0, y: int = 0, z: int = 0) -> 'Scanner':
        new_beacons = [Coord(x0+x, y0+y, z0+z) for (x0, y0, z0) in self.beacons]
        return self.__class__(
            number=self.number,
            beacons=new_beacons,
            location=self.location,
        )
    
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

    @cached_property
    def distance_map(self) -> dict[float, set[Coord]]:
        result = {}
        for b1, b2 in combinations(self.beacons, 2):
            x0, y0, z0 = b1
            x1, y1, z1 = b2
            d = sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2)
            if d not in result:
                result[d] = {b1, b2}
            else:
                result[d].add(b1)
                result[d].add(b2)
        return result

    @cached_property
    def coord_distances(self) -> dict[Coord, set[float]]:
        result = defaultdict(set)
        for b1, b2 in combinations(self.beacons, 2):
            x0, y0, z0 = b1
            x1, y1, z1 = b2
            d = sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2)
            result[b1].add(d)
            result[b2].add(d)
        return dict(result)

    @cached_property
    def distance_set(self) -> set[float]:
        result = set()
        for b1, b2 in combinations(self.beacons, 2):
            x0, y0, z0 = b1
            x1, y1, z1 = b2
            d = sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2)
            result.add(round(d, 3))
        return result
    
    def overlaps(self, other: 'Scanner', min_overlap: int = MIN_OVERLAP) -> bool:
        overlap = self.distance_set & other.distance_set
        return len(overlap) >= min_overlap

    def _correspondence(self, other: 'Scanner') -> dict[Coord, Coord]:
        correspondence = {}
        for c1, d1 in self.coord_distances.items():
            for c2, d2 in other.coord_distances.items():
                if len(d1 & d2) >= 11:
                    correspondence[c1] = c2
            # In theory, three should be enough, but not in certain arrangements.
            if len(correspondence) >= 5:
                return correspondence

    def reorient(self, other: 'Scanner') -> 'Scanner':
        '''
        Take another Scanner and orient it to the same grid system as this one.
        '''
        correspondence = self._correspondence(other)
        if correspondence is None:
            raise ValueError
        for c1, c2 in correspondence.items():
            # What is the common distance they share? 
            common_dists = self.coord_distances[c1] & other.coord_distances[c2]
            # If they don't have at least 11, this is probably a red herring.
            if len(common_dists) < 11:
                continue
            common_dist = next(iter(common_dists))
            # What point is on the other side of this distance line?
            c1_endpoints = [x for x in self.distance_map[common_dist] if x != c1]
            c2_endpoints = [x for x in other.distance_map[common_dist] if x != c2]
            if len(c1_endpoints) != 1 or len(c2_endpoints) != 1:
                continue
            c1_endpoint = c1_endpoints[0]
            c2_endpoint = c2_endpoints[0]
            # Construct the vectors from c1 and c2 to their "endpoints".
            x0, y0, z0 = c1
            x1, y1, z1 = c1_endpoint
            c1_vector = (x1-x0, y1-y0, z1-z0)
            x0, y0, z0 = c2
            x1, y1, z1 = c2_endpoint
            c2_vector = (x1-x0, y1-y0, z1-z0)
            # If any elements of the vector are 0, or the same as another, this vector
            # won't yield a distinct transformation.
            if 0 in c1_vector or 0 in c2_vector:
                continue
            if any(a == b for a, b in combinations(c1_vector, 2)):
                continue
            if any(a == b for a, b in combinations(c2_vector, 2)):
                continue
        # It was at this point that he realized he'd made a huge mistake by not using
        # matrix math to represent transformations of the grid.
        x1, y1, z1 = c1_vector
        x2, y2, z2 = c2_vector
        # First, which way are we now facing? This will get the z-coords matching.
        cls = other.__class__
        if abs(z1) == abs(z2):
            if z1 == z2:
                facing = lambda x: x
            else:
                facing = cls.facing_back
        elif abs(z1) == abs(y2):
            if z1 == y2:
                facing = cls.facing_up
            else:
                facing = cls.facing_down
        else: # abs(z1) == abs(x2):
            if z1 == z2:
                facing = cls.facing_left
            else:
                facing = cls.facing_right
        # To make life easier, transform c2_vector based on this facing before figuring
        # out rotation.
        c2_vector = facing(cls(number=0, beacons=[c2_vector])).beacons[0]
        x2, y2, z2 = c2_vector
        if z2 != z1:
            raise RuntimeError
        # Now figure out how to rotate to get x & y to match.
        if x1 == x2:
            rotate = lambda x: x
        elif x1 == y2:
            rotate = cls.rotated(3)
        elif x1 == -1 * x2:
            rotate = cls.rotated(2)
        else: # x1 == -y2:
            rotate = cls.rotated(1)
        # Transform c2 again to check our work
        c2_vector = rotate(cls(number=0, beacons=[c2_vector])).beacons[0]
        assert tuple(c2_vector) == c1_vector
        # Now we know we can apply these transformations to `other` to get it oriented
        # like self.
        other = rotate(facing(other))
        return other

    def find_offset(self, other: 'Scanner') -> tuple[int, int, int]:
        '''
        Determine the offset of one scanner from another.

        Adding the resulting tuple to each beacon of other will make put its coordinates
        on the same grid as self's. Assumes both scanners are already oriented the same
        way.
        '''
        correspondence = self._correspondence(other)
        if correspondence is None:
            raise ValueError
        # Grab an arbitrary mapping from self to other
        c1, c2 = next(iter(correspondence.items()))
        x1, y1, z1 = c1
        x2, y2, z2 = c2
        # It seems like it should be opposite (x2-x1) but experimentally, this is what
        # works.
        return (x1-x2, y1-y2, z1-z2)

    def __add__(self, other: 'Scanner') -> 'Scanner':
        other = self.reorient(other)
        offset = self.find_offset(other)
        other = other.offset(*offset)
        # Check that there are a bunch of overlapping points.
        return None

    def __iter__(self) -> Iterator[Coord]:
        return iter(self.beacons)

    def __str__(self) -> str:
        s = f'--- scanner {self.number} ---\n'
        for x, y, z in self.beacons:
            s += f'{x},{y},{z}\n'
        return s

    def __len__(self) -> int:
        return len(self.beacons)

    def grid(self) -> str:
        xs, ys, zs = zip(*self.beacons)
        x_bounds = min(xs), max(xs)
        y_bounds = min(ys), may(ys)
        z_bounds = min(zs), maz(zs)
        raise NotImplementedError
