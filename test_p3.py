# import pytest
from p3 import create_spiral, walk_spiral, create_mod_spiral

def test_spiral_starts():
    assert create_spiral(1) == [[1]]

def test_spiral_turns_right():
    assert create_spiral(2) == [[1,2]]
    assert create_spiral(8) == [[5,4,3],[6,1,2],[7,8]]
    assert create_spiral(9) == [[5,4,3],[6,1,2],[7,8,9]]
    assert create_spiral(10) == [[5,4,3],[6,1,2],[7,8,9,10]]
    assert create_spiral(23) == [[17,16,15,14,13],[18,5,4,3,12],[19,6,1,2,11],[20,7,8,9,10],[21,22,23]]

def test_spiral_turns_up():
    assert create_spiral(3) == [[3],[1,2]]
    assert create_spiral(11) == [[5,4,3],[6,1,2,11],[7,8,9,10]]
    assert create_spiral(12) == [[5,4,3,12],[6,1,2,11],[7,8,9,10]]
    assert create_spiral(13) == [[13],[5,4,3,12],[6,1,2,11],[7,8,9,10]]

def test_spiral_turns_left():
    assert create_spiral(4) == [[4,3],[1,2]]
    assert create_spiral(5) == [[5,4,3],[1,2]]
    assert create_spiral(14) == [[14,13],[5,4,3,12],[6,1,2,11],[7,8,9,10]]

def test_spiral_turns_down():
    assert create_spiral(6) == [[5,4,3],[6,1,2]]
    assert create_spiral(7) == [[5,4,3],[6,1,2],[7]]

def test_walk_spiral_from_center_to_center():
    assert walk_spiral(1) == 0

def test_walk_spiral_from_12_to_center():
    assert walk_spiral(12) == 3

def test_walk_spiral_from_23_to_center():
    assert walk_spiral(23) == 2

def test_walk_spiral_from_1024_to_center():
    assert walk_spiral(1024) == 31

def test_create_mod_spiral_2():
    assert create_mod_spiral(2) == [[1,1]]

def test_create_mod_spiral_3():
    assert create_mod_spiral(3) == [[2],[1,1]]

def test_create_mod_spiral_4():
    assert create_mod_spiral(4) == [[4,2],[1,1]]

def test_create_mod_spiral_5():
    assert create_mod_spiral(5) == [[5,4,2],[1,1]]

def test_create_mod_spiral_6():
    assert create_mod_spiral(6) == [[5,4,2],[10,1,1]]

def test_create_mod_spiral_7():
    assert create_mod_spiral(7) == [[5,4,2],[10,1,1],[11]]

def test_create_mod_spiral_8():
    assert create_mod_spiral(8) == [[5,4,2],[10,1,1],[11,23]]
