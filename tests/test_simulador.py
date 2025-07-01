import pytest
from src.celeste.vector3d import Vector3D
from src.celeste.simulador import Simulador

def test_agregar_y_listar(capsys):
    sim = Simulador()
    sim.agregar_cuerpo("A", 1.0, Vector3D(0, 0, 0), Vector3D(0, 0, 0))
    sim.listar_cuerpos()
    captured = capsys.readouterr()
    assert "A" in captured.out

def test_id_duplicado():
    sim = Simulador()
    sim.agregar_cuerpo("A", 1.0, Vector3D(0, 0, 0), Vector3D(0, 0, 0))
    with pytest.raises(ValueError):
        sim.agregar_cuerpo("A", 1.0, Vector3D(1, 0, 0), Vector3D(0, 0, 0))

def test_paso_simulacion_no_explota():
    sim = Simulador()
    sim.agregar_cuerpo("A", 1.0, Vector3D(0, 0, 0), Vector3D(0, 0, 0))
    sim.agregar_cuerpo("B", 1.0, Vector3D(1, 0, 0), Vector3D(0, 1, 0))
    sim.paso_simulacion(1.0)  # No debe lanzar excepciones
