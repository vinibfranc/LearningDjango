'''
condicao = 2 >= 2 #True = Loop infinito

while condicao:
	print('Executou')
else:
	print('Fim do loop')
'''

i = 0
while i < 10:
	if i == 5:
		'''i += 1
		continue'''
		break
	print(i)
	i += 1
else:
	print('Fim do loop')