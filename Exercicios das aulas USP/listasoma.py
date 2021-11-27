def soma_elementos(list):
	soma = 0
	for i in list:
		soma = soma + i
	return soma

lista = [36,88,3,1,5,44,]

print(soma_elementos(lista))