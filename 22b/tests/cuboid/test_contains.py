import sys

sys.path.append('.')

from cuboid import Cuboid

def test_non_overlap():
    a = Cuboid.from_string('x=3..7,y=1..2,z=-4..4')
    b = Cuboid.from_string('x=3..7,y=1..2,z=-8..-5')
    assert a not in b
    assert b not in a
    assert a.overlap(b) == 0
    assert b.overlap(a) == 0

test_non_overlap()

def test_complete_overlap():
    a = Cuboid.from_string('x=0..7,y=-11..-2,z=100..1000')
    b = Cuboid.from_string('x=3..7,y=-8..-7,z=101..104')
    assert a not in b
    assert b in a
    assert a.overlap(b) == 40
    assert b.overlap(a) == 40
    assert b.volume == 40

test_complete_overlap()

def test_some_overlap():
    a = Cuboid.from_string('x=6..7,y=-11..-6,z=100..102')
    b = Cuboid.from_string('x=3..7,y=-8..-7,z=101..104')
    assert a not in b
    assert b not in a
    assert a.overlap(b) == 8
    assert b.overlap(a) == 8

test_some_overlap()

def test_shared_border():
    a = Cuboid.from_string('x=3..7,y=-1..2,z=-40..-30')
    b = Cuboid.from_string('x=-1..3,y=-1..2,z=-40..-30')
    assert a not in b
    assert b not in a
    assert a.overlap(b) == 44
    assert b.overlap(a) == 44

test_shared_border()
