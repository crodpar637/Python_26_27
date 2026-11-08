def suma(a , b, *otros):
    total = a + b
    print("Otros:", otros)
    
    for n in otros:
        total += n

    # total += sum(otros)
    
    return total

print(suma(1,2,3,4,5,6,6))
print(suma(1,2,3,6))
print(suma(1,2))


