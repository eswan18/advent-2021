C_Range = tuple[int, int]
C_Slice = slice
C_Range_3d = tuple[C_Range, C_Range, C_Range]
C_Slice_3d = tuple[C_Slice, C_Slice, C_Slice]

DEFAULT_CUBOID_RANGES = (
    (-50, 50),
    (-50, 50),
    (-50, 50),
)

with open('test_input_a.txt', 'rt') as f:
    lines = [l.strip() for l in f.readlines()]

class Cuboid:
    def __init__(
        self,
        x_range: C_Range = DEFAULT_CUBOID_RANGES[0],
        y_range: C_Range = DEFAULT_CUBOID_RANGES[1],
        z_range: C_Range = DEFAULT_CUBOID_RANGES[2],
    ):
        self.x_range = x_range
        self.y_range = y_range
        self.z_range = z_range
        self._cubes = [
            [
                [False for _ in range(*x_range)]
                for _ in range(*y_range)
            ]
            for _ in range(*z_range)
        ]

    @property
    def x_min(self) -> int:
        return self.x_range[0]

    @property
    def y_min(self) -> int:
        return self.y_range[0]

    @property
    def z_min(self) -> int:
        return self.z_range[0]

    def _normalize_slices(self, slices: C_Slice_3d) -> C_Slice_3d:
        '''
        Adjust a cuboid range so we can use it as a direct index into self._cubes.

        Since ranges don't always (and usually don't) start at 0, they don't line up
        with our internal indices until adjusted.

        Also validate that all slice bounds are within the cuboid.
        '''
        # No steps allowed
        if not all(s.step is None for s in slices):
            raise TypeError
        # Adjust indices to be offset by how far in the negatives our ranges go.
        mins, maxes = zip(self.x_range, self.y_range, self.z_range)
        max_indices = tuple(max_-min_ for min_, max_ in zip(mins, maxes))
        result = tuple(
            slice(s.start - min_, s.stop - min_) for s, min_ in zip(slices, mins)
        )
        # Our cuboid is wildly unpythonic, and thus ranges are inclusive on both sides.
        result = tuple(slice(s.start, s.stop+1) for s in result)
        # Validation
        if not all (s.start >= 0 for s in result):
            raise ValueError('Bad start')
        if not all (s.stop <= (max_+1) for s, max_ in zip(result, max_indices)):
            raise ValueError('Bad stop')
        return result

    def __getitem__(self, key: C_Slice_3d) -> bool:
        x_range, y_range, z_range = self._normalize_slices(key)
        return [
            [column[x_range] for column in plane[y_range]]
            for plane in self._cubes[z_range]
        ]
        return self._cubes[z_range][y_range][x_range]

    def __setitem__(self, key: tuple[C_Range, C_Range, C_Range], on: bool) -> None:
        x_range, y_range, z_range = key
        for plane in self._cubes[z_range]:
            for column in plane[y_range]:
                column[x_range] = on

    def step(
        self,
        x_range: C_Range,
        y_range: C_Range,
        z_range: C_Range,
        on: bool,
    ) -> None:
        self[slice(*x_range), slice(*y_range), slice(*z_range)] = on

cube = Cuboid()

