valor = int(input("Digite o seu número inteiro:"))

valor_itt1 = valor % 3 

valor_itt2 = valor % 5

if (valor_itt1 == 0) and (valor_itt2 == 0):
  print ("FizzBuzz")
else:
  print(valor)