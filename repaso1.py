
#instruciones de entrada y salida
#print() o print(f)
#print('hola mundo')
#print(f'hola mundo numero {10}')
#entrada de datos
#input('escribe un numero')#se introduce solo letras
#casting para convertir a valores especificos
#f =0.0
#f = float(input('escribe numeros decimales'))
#a =0
#a = int(input('escribe un numero'))
#c =120
##print(str(c))
#v =""
#v = str(c)
#nota solo las variables que no se introduce por teclado se obliga a inicializarlas.
#hacer un programa que lea el nombre precio de un producto el programa calculara
#el costo y el precio de venta
#costo involucra el 12% y el iva !6%
#while(true)
for i in range(0,5):  #el rango valor incial hasta el valor final sin incluirlo
    precio = 12.55
    nombre = input('Ingrese el nombre del producto:\n')
    precio = float(input('ingrese el precio del producto: '))
    costo = precio * 1.12
    precioventa = costo * 1.16
    print(f'el costo es {costo :.2f} y el precio de venta {precioventa:.2f}')
    print(f'el costo es {costo} y el precio de venta {precioventa}')
    #res = input('deseas otro numero  (s/n)\n')
    #if res == 'n' or res == 'N':
    #    break
