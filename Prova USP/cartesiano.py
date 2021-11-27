import math

n1 = float (input("Digite o primeira coordenada:"))
n2 = float (input("Digite o segunda coordenada:"))
n3 = float (input("Digite o terceira coordenada:"))
n4 = float (input("Digite o quarta coordenada:"))


d = ((n1-n3)**2 + (n2-n4)**2)

dist = math.sqrt(d)

if dist >= 10 :
   print ("longe")
else:
  print ("perto")
