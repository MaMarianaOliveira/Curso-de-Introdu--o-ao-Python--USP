import math

a = float (input("Digite a variável a:"))
b= float(input("Digite a variável b:"))
c= float(input("Digite a variável c:"))

d = (b**2 - 4*a*c)


if (d > 0): 
   delta = math.sqrt(d)
   x1 = (-b + delta)/ (2*a)
   x2 = (-b - delta) / (2*a)
if (x1<x2):  
   print: ("as raízes da equação são", x1, "e", x2)
if (x1> x2): 
  print: ("as raízes da equação são", x2, "e", x1)

elif d==0:
  delta = math.sqrt(d)
  x = -b /(2*a)
  print ("Esse cálculo tem 1 raíz")
  print ( " X é", x) 

elif d < 0:
   print ("Essa raíz é imaginária!")
   print ( "Não existe X1 nem X2")
