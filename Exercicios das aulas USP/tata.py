n_salvo = n = int(input("Digite um numero: "))

anterior = n % 10
n = n // 10;
adj_iguais = False;
pos = 0

while n > 0 and not adj_iguais:
    atual = n % 10
    if atual == anterior:
        adj_iguais = True
    else:
        pos += 1
    anterior = atual
    n = n // 10

if adj_iguais:
   print ("sim")
else:
  print ("não")