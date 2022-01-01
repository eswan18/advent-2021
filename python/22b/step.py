from __future__ import annotations

from dataclasses import dataclass, field

from cuboid import Cuboid

@dataclass(frozen=True)
class Step:
    text: str = field(repr=False)
    on: bool
    cuboid: Cuboid

    @classmethod
    def from_string(cls, s: str) -> Step:
        on_str, cuboid_str = s.split(' ')
        on = True if on_str == 'on' else False
        cuboid = Cuboid.from_string(cuboid_str)
        return cls(text=s, on=on, cuboid=cuboid)


