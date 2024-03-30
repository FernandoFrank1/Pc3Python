# Problema 2

def main():
    calificaciones_entrantes = input("Ingrese las calificaciones separadas por comas(,): ")

    calificaciones_individuales = calificaciones_entrantes.split(',')

    lista_enteros = []

    try:
        for calificacion in calificaciones_individuales:
            calificacion_entero = int(calificacion.strip())
            
            if 0 <= calificacion_entero <= 20:
                lista_enteros.append(calificacion_entero)
            else:
                raise ValueError

        print("Las calificaciones como enteros son:", lista_enteros)

    except ValueError:
        print("ValueError: Se encontró un valor no válido. Asegúrese de ingresar solo números separados por comas y de 0 a 20.")


if __name__ == "__main__":
    main()