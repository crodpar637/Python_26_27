d= { 'a': 1, 'b':6}

print(d.get('a',None))
print(d.pop('d',None))

t = d.popitem()
print(t)

print(d)