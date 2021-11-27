valor = int(input("Digite o seu número inteiro:"))

rest = valor//5

valor_itt = valor % 5

if valor_itt == 0:
  print ("Buzz")
else:
  print(valor)