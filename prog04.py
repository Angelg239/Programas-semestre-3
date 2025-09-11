
# Crea una lista para guardar los números válidos.
a = [] 
# Creates a list to store the valid numbers.

# Variables para la suma y el conteo de números.
s = 0
n = 0
# Variables for the sum and number count.

# Cadena con los dígitos para la validación de entrada.
numeros = "0123456789"
# String with digits for input validation.

# Bucle para obtener 10 números válidos.
while n < 10:
    b = input('Escribe un número: ')
# Loop to get 10 valid numbers.
    
    # Se inicializa un contador para los caracteres numéricos.
    x = 0
    for i in b:
        if i in numeros:
            x += 1
    # A counter for numeric characters is initialized.

    # Si la longitud de la entrada es igual al conteo de dígitos, es un número válido.
    if len(b) == x:
        a.append(int(b))
        n += 1
    else:
    # If the input length equals the digit count, it's a valid number.

        # Si no, se informa al usuario.
        print('El valor no es un número válido')
        # Otherwise, the user is informed.

# Recorre la lista, imprime los números y calcula la suma.
for i in a:
    print(i)
    s += i
# Loops through the list, prints the numbers, and calculates the sum.

# Muestra el resultado final.
print(f'La suma es {s}')
# Displays the final result.
