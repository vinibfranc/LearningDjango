for i in range(1,11):
	print(i)
else:
	print('Fim do loop')

lista1 = {'Maca','Banana','Melao'}
lista2 = {'Tomate','Cebola','Cenoura'}

for i,j in zip(lista1, lista2):
	print(i,j)

for i,j in enumerate(lista1):
	print(i,j)