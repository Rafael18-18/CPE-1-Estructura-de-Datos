class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")
        print("----------------------")


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")

        contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(contacto)

        print("Contacto agregado correctamente.")

    def mostrar_contactos(self):
        if len(self.contactos) == 0:
            print("No existen contactos registrados.")
        else:
            for contacto in self.contactos:
                contacto.mostrar()

    def buscar_contacto(self):
        nombre = input("Ingrese el nombre a buscar: ")

        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                contacto.mostrar()
                return

        print("Contacto no encontrado.")

    def eliminar_contacto(self):
        nombre = input("Ingrese el nombre a eliminar: ")

        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print("Contacto eliminado.")
                return

        print("Contacto no encontrado.")


agenda = Agenda()

while True:
    print("\nAGENDA TELEFÓNICA")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agenda.agregar_contacto()

    elif opcion == "2":
        agenda.mostrar_contactos()

    elif opcion == "3":
        agenda.buscar_contacto()

    elif opcion == "4":
        agenda.eliminar_contacto()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")