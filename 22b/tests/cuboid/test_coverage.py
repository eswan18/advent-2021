import sys

sys.path.append('.')

from cuboid import Cuboid

def test_non_overlapping():
    a = Cuboid.from_string('x=3..7,y=1..2,z=-4..4')
    b = Cuboid.from_string('x=3..7,y=1..2,z=-8..-5')
    assert a.uncovered_volume([b]) == a.volume

test_non_overlapping()

def test_overlap2():
    a = Cuboid.from_string('x=-20..26,y=-36..17,z=-47..7')
    b = Cuboid.from_string('x=-20..33,y=-21..23,z=-26..28')
    assert b.uncovered_volume([a]) == 71328

test_overlap2()

def test_overlap3():
    a = Cuboid.from_string('x=-20..26,y=-36..17,z=-47..7')
    b = Cuboid.from_string('x=-20..33,y=-21..23,z=-26..28')
    c = Cuboid.from_string('x=-22..28,y=-29..23,z=-38..16')
    assert c.uncovered_volume([a, b]) == c.uncovered_volume([b, a]) == 14558

test_overlap3()

def test_overlap4():
    a = Cuboid.from_string('x=-20..26,y=-36..17,z=-47..7')
    b = Cuboid.from_string('x=-20..33,y=-21..23,z=-26..28')
    c = Cuboid.from_string('x=-22..28,y=-29..23,z=-38..16')
    d = Cuboid.from_string('x=-46..7,y=-6..46,z=-50..-1')
    print(d.uncovered_volume([a, b, c]))
    assert d.uncovered_volume([a, b, c]) == 102852
    assert d.uncovered_volume([c, b, a]) == 102852

test_overlap4()
