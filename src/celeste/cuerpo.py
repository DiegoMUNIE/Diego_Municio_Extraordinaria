from .vector3d import Vector3D

class CuerpoCeleste:
    def __init__(self, id: str, masa: float, posicion: Vector3D, velocidad: Vector3D):
        if masa <= 0:
            raise ValueError("La masa debe ser mayor que cero")
        self.id = id
        self.masa = masa
        self.posicion = posicion
        self.velocidad = velocidad
        self.fuerza = Vector3D(0, 0, 0)

    def aplicar_fuerza(self, f: Vector3D, dt: float):
        aceleracion = f * (1 / self.masa)
        self.velocidad = self.velocidad + aceleracion * dt

    def mover(self, dt: float):
        self.posicion = self.posicion + self.velocidad * dt

    def energia_cinetica(self):
        v = self.velocidad.magnitude()
        return 0.5 * self.masa * v**2

    def energia_potencial_con(self, otro, G):
        r = (self.posicion - otro.posicion).magnitude()
        return -G * self.masa * otro.masa / r if r != 0 else 0
