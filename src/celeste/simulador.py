import json
import csv
from .vector3d import Vector3D
from .cuerpo import CuerpoCeleste

class Simulador:
    def __init__(self, G=6.67430e-11):
        self.G = G
        self.cuerpos = {}

    def agregar_cuerpo(self, id, masa, posicion, velocidad):
        if id in self.cuerpos:
            raise ValueError("ID duplicado")
        self.cuerpos[id] = CuerpoCeleste(id, masa, posicion, velocidad)

    def listar_cuerpos(self):
        for c in self.cuerpos.values():
            print(f"{c.id}: masa={c.masa}, pos={c.posicion}, vel={c.velocidad}")

    def calcular_fuerzas(self):
        for c in self.cuerpos.values():
            c.fuerza = Vector3D(0, 0, 0)

        for i in self.cuerpos.values():
            for j in self.cuerpos.values():
                if i.id != j.id:
                    r_vec = j.posicion - i.posicion
                    dist = r_vec.magnitude()
                    if dist != 0:
                        fuerza_magn = self.G * i.masa * j.masa / dist**3
                        i.fuerza = i.fuerza + r_vec * fuerza_magn

    def paso_simulacion(self, dt):
        self.calcular_fuerzas()

        for c in self.cuerpos.values():
            c.aplicar_fuerza(c.fuerza, dt)

        for c in self.cuerpos.values():
            c.mover(dt)

        self.imprimir_energia_y_momento()

    def imprimir_energia_y_momento(self):
        K = sum(c.energia_cinetica() for c in self.cuerpos.values())
        U = sum(
            self.cuerpos[i].energia_potencial_con(self.cuerpos[j], self.G)
            for i in self.cuerpos
            for j in self.cuerpos
            if i < j
        )
        P = Vector3D(0, 0, 0)
        for c in self.cuerpos.values():
            P = P + c.velocidad * c.masa

        print("Energía cinética total:", K)
        print("Energía potencial total:", U)
        print(f"Momento lineal: {P}")

    def guardar(self, archivo):
        data = []
        for c in self.cuerpos.values():
            data.append({
                "id": c.id,
                "masa": c.masa,
                "posicion": [c.posicion.x, c.posicion.y, c.posicion.z],
                "velocidad": [c.velocidad.x, c.velocidad.y, c.velocidad.z]
            })
        if archivo.endswith(".json"):
            with open(archivo, 'w') as f:
                json.dump(data, f, indent=2)
        elif archivo.endswith(".csv"):
            with open(archivo, 'w', newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(["id", "masa", "x", "y", "z", "vx", "vy", "vz"])
                for d in data:
                    writer.writerow([
                        d["id"], d["masa"],
                        *d["posicion"], *d["velocidad"]
                    ])

    def cargar(self, archivo):
        self.cuerpos.clear()
        if archivo.endswith(".json"):
            with open(archivo) as f:
                data = json.load(f)
        elif archivo.endswith(".csv"):
            with open(archivo) as f:
                reader = csv.DictReader(f, delimiter=';')
                data = [
                    {
                        "id": row["id"],
                        "masa": float(row["masa"]),
                        "posicion": [float(row["x"]), float(row["y"]), float(row["z"])],
                        "velocidad": [float(row["vx"]), float(row["vy"]), float(row["vz"])]
                    }
                    for row in reader
                ]
        for d in data:
            self.agregar_cuerpo(
                d["id"], d["masa"],
                Vector3D(*d["posicion"]),
                Vector3D(*d["velocidad"])
            )
