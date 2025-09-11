
# hacer un programa que lea 10 numeros y los almacene en un arreglo

# Se inicializa una lista 'a' con 9 elementos, todos con el valor 0.
# Es importante notar que la lista solo tiene 9 elementos, no 10.
a = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# This initializes a list 'a' with 9 elements, all with the value 0.
# It's important to note that the list only has 9 elements, not 10.

# Este ciclo for intenta iterar 10 veces para pedir números al usuario.
# Sin embargo, debido a que la lista 'a' solo tiene 9 elementos (índices 0-8),
# el código generará un error de "índice fuera de rango" en la última
# iteración (cuando i = 9).
for i in range(10):
    a[i] = int(input('Escribe un número \n'))
# This for loop attempts to iterate 10 times to ask the user for numbers.
# However, because list 'a' only has 9 elements (indexes 0-8),
# the code will produce an "index out of range" error on the last
# iteration (when i = 9).

# Este ciclo for recorre la lista 'a' y muestra cada uno de sus elementos.
# Si el código de arriba genera un error, este ciclo no se ejecutará.
for i in a:
    print(i)
# This for loop iterates through the list 'a' and prints each of its elements.
# If the code above throws an error, this loop will not be executed.