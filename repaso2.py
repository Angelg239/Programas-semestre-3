
a = 0
b = 0
c = 0
m = 0
r = 0
ra = 0.0
d = 0.0
x1 = 0.0
x2 = 0.0

# Aquí deberías pedir los valores de a, b, c
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

p = b ** 2
m = 4 * a * c
r = p - m

if r > 0:
    print('sí se puede, hay dos soluciones reales')
    ra = r ** (1/2)
    d = 2 * a
    x1 = (-b + ra) / d
    x2 = (-b - ra) / d
    print(f'el valor de x1 es {x1:.2f} y el valor de x2 es {x2:.2f}')
else:
    print('no se puede, no hay soluciones reales')
