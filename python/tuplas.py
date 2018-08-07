a = 10
b = 1,2,3,4, ('asdf',2,'a'), 1.2, 'asd'
print(type(b))
print(b)
print(b[4][0])

print(b.count(2))
print(b.index(('asdf',2,'a')))


for i in b:
	print(i)

i = 0
while i < len(b):
	print(b[i])
	i += 1

c = (10,20,30)
print(c)
print(c[0])

