t= n = int(input("Digite o número inteiro : "))

outro = n % 10
n = n // 10;
y = False;
pos = 0

while n > 0 and not y : 
  atual = n % 10
  if atual == outro:
    y = True
  else:
    pos += 1
  outro = atual
  n = n //10
if y : 
 print ("sim")
else:
 print ("não")
    