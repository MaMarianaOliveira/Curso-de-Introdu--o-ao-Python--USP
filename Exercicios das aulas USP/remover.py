def remove_repetidos(lista):
	l = []
	for i in lista:
		if i not in l:
			l.append(i)
	l.sort()
	return l


lista = [1,3,5,2,4,2,1,6,7,2,8,6]

lista = remove_repetidos(lista)
print (lista)
