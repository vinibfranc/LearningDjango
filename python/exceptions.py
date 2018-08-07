try:
	1 / 0
except(Exception, ZeroDivisionError) as e:
	print(e)
else: # executado se não tem exceção
	print('Sem exceção')
finally: # executado se tem ou não exceção
	print('Finally')