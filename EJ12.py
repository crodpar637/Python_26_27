from math import sqrt

# Escriba un programa que resuelva la ecuación cuadrática (ax2 + bx + c =0) mostrando sus
# soluciones o indicando que no tiene solución cuando así sea.

a = int(input("Coeficiente a:"))
b = int(input("Coeficiente b:"))
c = int(input("Coeficiente c:"))

discriminante = b * b - 4 * a *c

if discriminante < 0:
    print ("Con estos coeficientes no hay solución")
else:
    sol1 = (- b + sqrt(discriminante) ) / (2 * a)
    sol2 = (- b - sqrt(discriminante) ) / (2 * a)

    if sol1 == sol2:
        print("La única solución es:" , sol1)
    else:
        print("La primera solución es:", sol1)
        print("La segunda solución es:", sol2)












               
    