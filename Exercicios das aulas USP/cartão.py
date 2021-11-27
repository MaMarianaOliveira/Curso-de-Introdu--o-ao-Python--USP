

meuCartao = int (input("Digite o número do seu cartão de crédito:"))

cartaoLido = 1
encontreiMeuCartao = False

while cartaoLido != 0 and not encontreiMeuCartao :
	cartaoLido = int (input("Digite o número do próximo cartão de crédito:"))
	if cartaoLido == meuCartao:
		encontreiMeuCartao = True

if encontreiMeuCartao:
	print("EBAA!! Meu cartão está lá!")
else:
	print ("Xi, meu cartão não está lá!")
