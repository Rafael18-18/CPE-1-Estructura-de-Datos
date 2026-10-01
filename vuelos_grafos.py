import heapq
import time


# ============================================================
# BASE DE DATOS FICTICIA DE VUELOS
# ============================================================

vuelos = [
    ("Quito", "Guayaquil", 85),
    ("Quito", "Cuenca", 40),
    ("Quito", "Loja", 70),
    ("Quito", "Manta", 65),

    ("Cuenca", "Guayaquil", 35),
    ("Cuenca", "Loja", 45),

    ("Loja", "Guayaquil", 60),
    ("Loja", "Cuenca", 45),

    ("Manta", "Guayaquil", 30),

    ("Guayaquil", "Quito", 85),
    ("Guayaquil", "Manta", 30),

    ("Ambato", "Quito", 35),
    ("Ambato", "Riobamba", 25),

    ("Riobamba", "Quito", 40),
    ("Riobamba", "Cuenca", 30)
]


# ============================================================
# CREAR EL GRAFO
# ============================================================

def crear_grafo():
    grafo = {}

    for origen, destino, precio in vuelos:

        # Crear la ciudad de origen si no existe
        if origen not in grafo:
            grafo[origen] = []

        # Crear la ciudad de destino si no existe
        if destino not in grafo:
            grafo[destino] = []

        # Agregar la conexión
        grafo[origen].append((destino, precio))

    return grafo


# ============================================================
# MOSTRAR TODOS LOS VUELOS
# ============================================================

def mostrar_vuelos():
    print("\n" + "=" * 55)
    print("                 VUELOS DISPONIBLES")
    print("=" * 55)

    for origen, destino, precio in vuelos:
        print(f"{origen:12} -> {destino:12} | ${precio:.2f}")

    print("=" * 55)


# ============================================================
# MOSTRAR EL GRAFO
# ============================================================

def mostrar_grafo(grafo):
    print("\n" + "=" * 55)
    print("                 GRAFO DE VUELOS")
    print("=" * 55)

    for ciudad in grafo:
        print(f"\n{ciudad}:")

        if len(grafo[ciudad]) == 0:
            print("   Sin conexiones")

        else:
            for destino, precio in grafo[ciudad]:
                print(f"   -> {destino} (${precio:.2f})")

    print("=" * 55)


# ============================================================
# ALGORITMO DE DIJKSTRA
# ============================================================

def dijkstra(grafo, origen, destino):

    # Inicializar todas las distancias como infinito
    distancias = {}

    # Guardar la ciudad anterior para reconstruir la ruta
    anteriores = {}

    for ciudad in grafo:
        distancias[ciudad] = float("inf")
        anteriores[ciudad] = None

    # La distancia desde el origen hacia sí mismo es 0
    distancias[origen] = 0

    # Cola de prioridad
    cola = [(0, origen)]

    while cola:

        # Obtener la ciudad con menor distancia
        distancia_actual, ciudad_actual = heapq.heappop(cola)

        # Si ya tenemos una distancia menor, ignoramos este dato
        if distancia_actual > distancias[ciudad_actual]:
            continue

        # Revisar todas las conexiones
        for vecino, precio in grafo[ciudad_actual]:

            nueva_distancia = distancia_actual + precio

            # Si encontramos una ruta más barata
            if nueva_distancia < distancias[vecino]:

                distancias[vecino] = nueva_distancia
                anteriores[vecino] = ciudad_actual

                heapq.heappush(
                    cola,
                    (nueva_distancia, vecino)
                )

    # Comprobar si existe una ruta
    if distancias[destino] == float("inf"):
        return None, None

    # Reconstruir la ruta
    ruta = []

    ciudad_actual = destino

    while ciudad_actual is not None:
        ruta.append(ciudad_actual)
        ciudad_actual = anteriores[ciudad_actual]

    # La ruta se construye desde el destino hacia el origen,
    # por eso debemos invertirla
    ruta.reverse()

    return ruta, distancias[destino]


# ============================================================
# BUSCAR EL VUELO MÁS BARATO
# ============================================================

def buscar_vuelo(grafo):

    print("\n" + "=" * 55)
    print("              BUSCAR VUELO MÁS BARATO")
    print("=" * 55)

    origen = input("Ingrese la ciudad de origen: ").strip().title()
    destino = input("Ingrese la ciudad de destino: ").strip().title()

    # Verificar que las ciudades existan
    if origen not in grafo:
        print("\nERROR: La ciudad de origen no existe.")
        return

    if destino not in grafo:
        print("\nERROR: La ciudad de destino no existe.")
        return

    if origen == destino:
        print("\nEl origen y destino son la misma ciudad.")
        return

    # Iniciar medición del tiempo
    inicio = time.perf_counter()

    # Ejecutar Dijkstra
    ruta, costo = dijkstra(grafo, origen, destino)

    # Finalizar medición
    fin = time.perf_counter()

    tiempo = fin - inicio

    # Mostrar resultado
    print("\n" + "=" * 55)
    print("                    RESULTADO")
    print("=" * 55)

    if ruta is None:
        print("No existe una ruta disponible entre esas ciudades.")

    else:
        print("Ruta más barata:")

        print(" -> ".join(ruta))

        print(f"\nCosto total: ${costo:.2f}")

        print(f"Tiempo de ejecución: {tiempo:.8f} segundos")

    print("=" * 55)


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def menu():

    # Crear el grafo
    grafo = crear_grafo()

    while True:

        print("\n")
        print("=" * 55)
        print("             SISTEMA DE VUELOS BARATOS")
        print("=" * 55)
        print("1. Mostrar vuelos disponibles")
        print("2. Mostrar grafo")
        print("3. Buscar vuelo más barato")
        print("4. Salir")
        print("=" * 55)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":

            mostrar_vuelos()

        elif opcion == "2":

            mostrar_grafo(grafo)

        elif opcion == "3":

            buscar_vuelo(grafo)

        elif opcion == "4":

            print("\nPrograma finalizado correctamente.")
            break

        else:

            print("\nERROR: Opción no válida.")
            print("Seleccione una opción del 1 al 4.")


# ============================================================
# INICIO DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    menu()