#Escriba un programa que calcule la suma de todos los números que sean divisible por 3 y por 7
#entre el número 1 y el 1000

suma = 0

for i in range(1,1001):
    if i % 3 == 0 and i % 7 == 0 :
        suma += i

print("El resultado es:", suma)