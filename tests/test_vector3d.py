import pytest
from src.celeste.vector3d import Vector3D

def test_add():
    v1 = Vector3D(1,2,3)
    v2 = Vector3D(4,5,6)
    assert (v1 + v2).x == 5
    assert (v1 + v2).y == 7
    assert (v1 + v2).z == 9

def test_magnitude():
    v = Vector3D(3, 4, 0)
    assert v.magnitude() == 5
