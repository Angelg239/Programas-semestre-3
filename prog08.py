
#primera letramayuscukla
#no se aceptan espacios
n = 0
c = []   # lista donde se guardarán las cadenas válidas

while n < 5:
    dato = input('Escribe una cadena:\n')

    # Verificar si contiene espacios
    if " " in dato:
        print('No se aceptan espacios, intenta de nuevo')
        continue

    # Otra forma: usando replace
    if len(dato) > 0:
        primera = dato[0].upper()
        dato = dato.replace(dato[0], primera, 1)  # solo la primera ocurrencia

    c.append(dato)  # guardamos la cadena válida
    n += 1

print("\nLas cadenas ingresadas son:")
print(c)
