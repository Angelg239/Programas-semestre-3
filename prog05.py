
# Hacer un programa que lea 10 datos.
# Si el dato es un número se almacenará en un arreglo (lista fija).
# Si es un carácter o varios, se pondrá en otra lista.
# Al final, se mostrará cuántos números y cuántos caracteres se ingresaron.

numeros = [0,0,0,0,0,0,0,0,0,0]
b = []
n = 0
e = 0

  
for i in range(10):
    dato = input('Ingrese un dato:\n')
    

    if dato.isdigit():                
        numeros[n] = int(dato)
        n +=1
       
    else:
        b.append(dato)
        e += 1
 
# Mostrar resultados
print("\nRESULTADOS")
print("Números en arreglo:")
for i in range(n):
    print(numeros[i])

print("\nCaracteres de la lista:")
for i in b:
    print(i)

print(f"\nCantidad de números: {n}")
print(f"Cantidad de caracteres: {e}")
