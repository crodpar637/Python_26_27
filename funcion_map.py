l = [1,2,3]

x = map(lambda x: x+1, l)

l.append(4)
l.append(5)

print(x)

for elem in x:
    print(elem)

x = map(lambda x: x+1, l)
l2 = list(x)

print(l2)
print(l2)
print(l2)

l = [1,2,3]
l3 = [ n ** 2 for n in l]
print("l3:", l3)

l4 = ( n ** 2 for n in l)
print("l4:", l4, "list(l4):", list(l4))










