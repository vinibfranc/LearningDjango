d = {'nome':'Fulano','idade':18}
print(d['nome'])
print(d['idade'])
d['salario'] = 5000
print(d)
print(d.keys())
print(d.values())

d2 = {'rua': 'rua tal','bairro':'bairro x'}
d.update(d2)
print(d)

d.setdefault('Ciclano','Não encontrado')
print(d)

d.popitem()
print(d)

d.pop('salario')
print(d)

d.get('idade',18)

d.fromkeys([1,2,3],'x')

d.copy()

for i in d:
	print(i)
