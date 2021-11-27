#Treino de While dentro de While
n = int(input( "Digite o valor de n : "))

while n>=0:
	fat = 1
	while n > 1 :
  		fat = fat*n
  		n = n - 1

	print (fat)
	n = int(input( "Digite o valor de n : "))
	