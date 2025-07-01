from .vector3d import Vector3D
from .simulador import Simulador

def leer_vector(prompt):
    try:
        valores = list(map(float, input(prompt).split()))
        if len(valores) != 3:
            raise ValueError
        return Vector3D(*valores)
    except ValueError:
        print("Debe ingresar exactamente tres números separados por espacios.")
        return leer_vector(prompt)

def main():
    sim = Simulador()

    while True:
        print("\n--- Simulador Celeste ---")
        print("1. Listar cuerpos")
        print("2. Agregar cuerpo")
        print("3. Ejecutar paso de simulación")
        print("4. Guardar sistema")
        print("5. Cargar sistema")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sim.listar_cuerpos()
        elif opcion == "2":
            id = input("ID del cuerpo: ")
            masa = float(input("Masa (kg): "))
            posicion = leer_vector("Posición inicial (x y z): ")
            velocidad = leer_vector("Velocidad inicial (vx vy vz): ")
            try:
                sim.agregar_cuerpo(id, masa, posicion, velocidad)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == "3":
            dt = float(input("Δt (en segundos): "))
            sim.paso_simulacion(dt)
        elif opcion == "4":
            archivo = input("Nombre de archivo (.json o .csv): ")
            sim.guardar(archivo)
        elif opcion == "5":
            archivo = input("Nombre de archivo (.json o .csv): ")
            try:
                sim.cargar(archivo)
                print("Sistema cargado.")
            except Exception as e:
                print(f"Error al cargar: {e}")
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
