import pytest
from src.celeste.vector3d import Vector3D
from src.celeste.cuerpo import CuerpoCeleste

def test_creacion_valida():
    pos = Vector3D(0, 0, 0)
    vel = Vector3D(1, 0, 0)
    c = CuerpoCeleste("tierra", 5.972e24, pos, vel)
    assert c.id == "tierra"
    assert c.masa == 5.972e24

def test_masa_invalida():
    with pytest.raises(ValueError):
        CuerpoCeleste("error", 0, Vector3D(0, 0, 0), Vector3D(0, 0, 0))

def test_energia_cinetica():
    c = CuerpoCeleste("test", 2.0, Vector3D(0, 0, 0), Vector3D(3, 0, 0))
    assert c.energia_cinetica() == pytest.approx(9.0)

def test_aplicar_fuerza():
    c = CuerpoCeleste("f", 1.0, Vector3D(0, 0, 0), Vector3D(0, 0, 0))
    fuerza = Vector3D(1, 0, 0)
    c.aplicar_fuerza(fuerza, 1)
    assert c.velocidad.x == 1.0

def test_mover():
    c = CuerpoCeleste("m", 1.0, Vector3D(0, 0, 0), Vector3D(1, 2, 3))
    c.mover(2)
    assert c.posicion == Vector3D(2, 4, 6)
