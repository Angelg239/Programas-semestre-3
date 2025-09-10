
#hacer un programa que lea nombre edad y sexo de 5 personas,estos elementos deben estar dentro de una lista


def inicio():
    l=0
while True:
    aux = 0
    b = input('Ingrese la edad:\n')
    c = input('ingrese el sexo')
    d = input('escribe el genero')
    aux + 'nombre:' + b +'edad:' + c + 'genero' + d
    list.append(aux)
    c+=1
    if c>=5:
        break
   
print(list)


list =[]

if __name__ == "__main__": #metodo principal
 inicio()



