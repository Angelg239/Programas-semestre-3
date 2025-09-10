
# hacer que lea una cadena y que muestre en pantalla cuantos numeros tienes y
# cuantas mayusculas, cuantas minusculas y cuantos espacios

def inicio():
    mi = 0   # minusculas
    may = 0  # mayusculas
    c = 0    # numeros
    e = 0    # espacios

    numero = "0123456789"
    cadena = input('Escribe una cadena\n')

    for i in cadena:
        if i in numero:             # si es número
            print('es número')
            c += 1
        elif ord(i) == 32:          # si es espacio
            e += 1
        elif 97 <= ord(i) <= 122:   # si es minúscula
            mi += 1
        elif 65 <= ord(i) <= 90:    # si es mayúscula
            may += 1

    print(f'Los números son: {c}')
    print(f'Los espacios son: {e}')
    print(f'Las mayúsculas son: {may}')
    print(f'Las minúsculas son: {mi}')


if __name__ == '__main__':  # método principal
    inicio()
