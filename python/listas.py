a = [1, 2, 3]
print(type(a))
a.append(4)
print(a)
b = a.copy()
print(b)
c = a
print(c)
a.append(1)
print(a)
print(a.count(1))
print(a.index(4))
a.insert(3,'Novo valor')
print(a)
a.remove('Novo valor')
print(a)
c = a.remove(4)
print(c)
a.reverse()
print(a)
a.sort()
print(a)
b.clear()
print(b)



