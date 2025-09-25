
#def validar(a):
   # c = 0
    #d = 0.0
    #try:
     #   c = int(a)
      #  print('Es un valor numerico sin decimales')
    #except ValueError:
     #   print('No es un valor numerico con decimales')
    
    #try:
     #   d = float(a)
      #  print('Es un valor numerico con decimales')
    #except ValueError:
     #   print('No es un valor con decimales')

#def leer():
    # ord que obtiene el ascii del caracter
    # isalpha para caracteres
    # isdigit para numeros
    # try except ValueError
 #   a = input('Escribe un dato o valor')
  #  validar(a)

# Hacer un programa que lea un dato y que lo almacene en un lista respetando su tipo de dato
def validar(a):
   nf = 0
   ne = 0
   try:
      ne = int(a)
      return ne
   except ValueError:
      print('No es un entero')

def leer():
    a = input('Escribe un dato \n')
    dato = validar(a)
    lista.append(dato)

lista = []

if __name__=='__mian__':
    while(True):
      leer()
      res = input('Desea otro s/n')
      if res == 'n' or res == 'N':
         print(lista)
         break