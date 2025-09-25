
def vocales(cad):
   ba = False
   be = False
   bi = False
   bo = False
   bu = False
   
   if 'a' in cad or 'A' in cad:
       ba = True
   if 'e' in cad or 'E' in cad:
       be = True
   if 'i' in cad or 'I' in cad:
       bi = True
   if 'o' in cad or 'O' in cad:
       bo = True
   if 'u' in cad or 'U' in cad:
       bu = True

   if ba == True and be == True and bi == True and bo == True and bu == True:
       print("La cadena contiene todas las vocales")
   else:
       print("La cadena NO contiene todas las vocales")


def minusculas(c):
    cm = 0
    print(c)
    for i in c[1:]:
        if ord(i) >= 97 and ord(i) <= 122:
            cm += 1
    if cm == len(c) - 1:
        print(f"La cadena son minÃºsculas menos la primera {cm}")
        vocales(c)
    else:
        print("Error: la cadena no cumple")
             

def leer():
    ce = 0   # antes no estaba inicializada
    nc = ""
    c = input("Escribe una cadena: ")
     
    for i in c:
        if ord(i) != 32:
            ce += 1

    if ce == len(c):
        if c.isalpha():
            minusculas(c)
        else:
            for i in c:
                if ord(i) >= 48 and ord(i) <= 57:
                    pass
                else:
                    nc += i
            print(nc)
            minusculas(nc)
            print("Error: la cadena no cumple")
    else:
        print("Error: la cadena no cumple (espacios detectados)")


lista = []
if __name__ == "__main__":
    while True:
        leer()
        lista.append(1)  # algo para que cuente
        if len(lista) >= 5:
            break
