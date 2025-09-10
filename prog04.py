
a = []      # Lista para almacenar los números
s = 0       # Suma de los números
n = 0       # Contador de números válidos
numeros = "0123456789"

while n < 10:
    b = input('Escribe un número: ') 
    x = 0
#if(ord(i)>= 48 and ord(i) <=57):
    
    for i in b:    
        if i in numeros:
            x += 1

    # Si todos los caracteres del input son números
    if len(b) == x:
        a.append(int(b))
        n += 1
    else:
        print('El valor no es número válido')


# Mostrar resultados

for i in a:
    print(i)
    s += i

print(f'La suma es {s}')
