
# hacer un programa que lea 10 numeros y los almacene en un arreglo

a = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    a[i] = int(input('Escribe un número \n'))

for i in a:
    print(i)