# Problema 5

class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No especificada")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No especificadas")

    def set_age(self, edad):
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError("La edad no puede ser negativa.")
            self.edad = edad
        except ValueError:
            print("ValueError: La edad debe ser un número entero.")

    def set_nota(self, nota):
        try:
            nota = float(nota)
            if nota <= 0 or nota >= 20:
                raise ValueError("La nota debe estar entre 0 y 20.")
            self.notas.append(nota)
        except ValueError:
            print("ValueError: La nota debe ser un número válido entre 0 y 20.")


if __name__ == "__main__":
    nombre = input("Ingrese el nombre del estudiante: ")
    if not nombre.replace(" ", "").isalpha():
        print("Error: El nombre solo puede contener letras.")
    else:
        while True:
            numero_registro = input("Ingrese el número de registro del estudiante: ")
            if not numero_registro.isdigit():
                print("Error: El número de registro debe ser un valor numérico.")
            else:
                break
        
        alumno = Alumno(nombre, numero_registro)

        alumno.display()

        while True:
            edad = input("Ingrese la edad del estudiante: ")
            if not edad.isdigit():
                print("Error: La edad debe ser un número entero.")
            else:
                alumno.set_age(edad)
                break

        while True:
            nota = input("Ingrese notas del estudiante de 0 a 20 (o 'fin' para terminar): ")
            if nota.lower() == "fin":
                break
            alumno.set_nota(nota)

        alumno.display()
