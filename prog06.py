
def resultados(numeros, b, n, e):
    print('\nResultado')
    print('Números en arreglo:')
    for i in range(n):
        print(numeros[i])
    
    print('\nCaracteres de la lista:')
    for i in b:
        print(i)
    
    print(f'\nCantidad de números: {n}')
    print(f'Cantidad de caracteres: {e}')

def inicio():
    # Global variables must be declared as such to be modified inside a function.
    global numeros, b, n, e
    
    print('hola mundo')
    for i in range(10):
        dato = input('Ingrese un dato:\n')
        
        if dato.isdigit():
            numeros[n] = int(dato)
            n += 1
        else:
            b.append(dato)
            e += 1
    
    resultados(numeros, b, n, e)

# Initializing global variables outside of any function.
numeros = [0] * 10
b = []
n = 0
e = 0

if __name__ == "__main__":
    inicio()
