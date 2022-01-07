import sys

sys.path.append('.')

from bound import Bound

def test_non_overlap():
    a = Bound(3, 7)
    b = Bound(8, 10)
    assert a not in b
    assert b not in a
    assert a.overlap(b) == 0
    assert b.overlap(a) == 0

test_non_overlap()

def test_complete_overlap():
    a = Bound(-4, 3)
    b = Bound(0, 1)
    assert a not in b
    assert b in a
    assert a.overlap(b) == 2
    assert b.overlap(a) == 2

test_complete_overlap()

def test_some_overlap():
    a = Bound(-34, -13)
    b = Bound(-15, -5)
    assert a not in b
    assert b not in a
    assert a.overlap(b) == 3
    assert b.overlap(a) == 3

test_some_overlap()

def test_some_overlap2():
    a = Bound(-34, -15)
    b = Bound(-15, -5)
    assert a not in b
    assert b not in a
    assert a.overlap(b) == 1
    assert b.overlap(a) == 1

test_some_overlap2()

def test_shared_border():
    a = Bound(-34, -13)
    b = Bound(-13, 0)
    assert a not in b
    assert b not in a
    assert a.overlap(b) == 1
    assert b.overlap(a) == 1

test_shared_border()

def test_regression():
    a = Bound(-26, 28)
    b = Bound(-50, -1)
    assert a not in b
    assert b not in a
    assert a.overlap(b) == 26
    assert b.overlap(a) == 26

test_regression()
