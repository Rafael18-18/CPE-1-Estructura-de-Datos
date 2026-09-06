import time


# ==============================
# DATOS DEL TORNEO
# ==============================

# CONJUNTO: almacena los equipos sin permitir duplicados
equipos = {
    "Barcelona FC",
    "Real Madrid",
    "Manchester City"
}

# MAPA/DICCIONARIO: relaciona cada equipo con sus jugadores
jugadores_por_equipo = {
    "Barcelona FC": {
        "Carlos Pérez",
        "Luis Gómez",
        "Andrés Torres"
    },
    "Real Madrid": {
        "Juan Rodríguez",
        "Pedro Sánchez",
        "Miguel López"
    },
    "Manchester City": {
        "David García",
        "Daniel Martínez",
        "Jorge Castro"
    }
}

# DICCIONARIO: información de cada jugador
jugadores = {
    "Carlos Pérez": {
        "edad": 21,
        "posición": "Delantero",
        "goles": 4
    },
    "Luis Gómez": {
        "edad": 23,
        "posición": "Mediocampista",
        "goles": 2
    },
    "Andrés Torres": {
        "edad": 20,
        "posición": "Defensa",
        "goles": 1
    },
    "Juan Rodríguez": {
        "edad": 24,
        "posición": "Delantero",
        "goles": 5
    },
    "Pedro Sánchez": {
        "edad": 22,
        "posición": "Mediocampista",
        "goles": 3
    },
    "Miguel López": {
        "edad": 25,
        "posición": "Defensa",
        "goles": 1
    },
    "David García": {
        "edad": 23,
        "posición": "Delantero",
        "goles": 6
    },
    "Daniel Martínez": {
        "edad": 21,
        "posición": "Mediocampista",
        "goles": 4
    },
    "Jorge Castro": {
        "edad": 26,
        "posición": "Defensa",
        "goles": 2
    }
}


# ==============================
# FUNCIONES
# ==============================

def mostrar_equipos():
    print("\n===== EQUIPOS REGISTRADOS =====")

    for equipo in sorted(equipos):
        print("-", equipo)


def mostrar_jugadores():
    print("\n===== JUGADORES POR EQUIPO =====")

    for equipo, jugadores_equipo in jugadores_por_equipo.items():
        print(f"\n{equipo}:")
        for jugador in sorted(jugadores_equipo):
            print("  -", jugador)


def buscar_jugador():
    nombre = input("\nIngrese el nombre del jugador: ")

    if nombre in jugadores:
        datos = jugadores[nombre]

        print("\n===== INFORMACIÓN DEL JUGADOR =====")
        print("Nombre:", nombre)
        print("Edad:", datos["edad"])
        print("Posición:", datos["posición"])
        print("Goles:", datos["goles"])

        # MAPA INVERSO: localizar el equipo del jugador
        for equipo, lista_jugadores in jugadores_por_equipo.items():
            if nombre in lista_jugadores:
                print("Equipo:", equipo)
                break
    else:
        print("Jugador no encontrado.")


def registrar_jugador():
    nombre = input("\nNombre del nuevo jugador: ")

    if nombre in jugadores:
        print("El jugador ya está registrado.")
        return

    print("\nEquipos disponibles:")
    for equipo in sorted(equipos):
        print("-", equipo)

    equipo = input("Ingrese el equipo: ")

    if equipo not in equipos:
        print("El equipo no existe.")
        return

    edad = int(input("Edad: "))
    posicion = input("Posición: ")
    goles = int(input("Goles: "))

    # Se agrega al diccionario
    jugadores[nombre] = {
        "edad": edad,
        "posición": posicion,
        "goles": goles
    }

    # Se agrega al conjunto del equipo
    jugadores_por_equipo[equipo].add(nombre)

    print("Jugador registrado correctamente.")


def reporte_goleadores():
    print("\n===== REPORTE DE GOLEADORES =====")

    goleadores = sorted(
        jugadores.items(),
        key=lambda x: x[1]["goles"],
        reverse=True
    )

    for posicion, (nombre, datos) in enumerate(goleadores, start=1):
        print(
            f"{posicion}. {nombre} - "
            f"{datos['goles']} goles - "
            f"{datos['posición']}"
        )


def analizar_conjuntos():
    print("\n===== ANÁLISIS DE CONJUNTOS =====")

    equipo1 = jugadores_por_equipo["Barcelona FC"]
    equipo2 = jugadores_por_equipo["Real Madrid"]

    print("Jugadores de Barcelona FC:")
    print(equipo1)

    print("\nJugadores de Real Madrid:")
    print(equipo2)

    # INTERSECCIÓN
    comunes = equipo1.intersection(equipo2)

    print("\nJugadores compartidos:")
    print(comunes)

    # UNIÓN
    todos = equipo1.union(equipo2)

    print("\nJugadores de ambos equipos:")
    print(todos)


def analizar_tiempo():
    inicio = time.perf_counter()

    for _ in range(100000):
        "Carlos Pérez" in jugadores

    fin = time.perf_counter()

    tiempo = fin - inicio

    print("\n===== ANÁLISIS DEL TIEMPO =====")
    print(f"Tiempo de 100000 búsquedas: {tiempo:.6f} segundos")


def menu():
    while True:
        print("\n")
        print("======================================")
        print("      SISTEMA DE TORNEO DE FÚTBOL")
        print("======================================")
        print("1. Mostrar equipos")
        print("2. Mostrar jugadores")
        print("3. Buscar jugador")
        print("4. Registrar jugador")
        print("5. Reporte de goleadores")
        print("6. Operaciones con conjuntos")
        print("7. Analizar tiempo de ejecución")
        print("8. Salir")
        print("======================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_equipos()

        elif opcion == "2":
            mostrar_jugadores()

        elif opcion == "3":
            buscar_jugador()

        elif opcion == "4":
            registrar_jugador()

        elif opcion == "5":
            reporte_goleadores()

        elif opcion == "6":
            analizar_conjuntos()

        elif opcion == "7":
            analizar_tiempo()

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    menu()