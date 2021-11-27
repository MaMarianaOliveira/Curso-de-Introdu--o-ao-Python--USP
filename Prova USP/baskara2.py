import math

a = float (input("Digite a variável a:"))
b= float(input("Digite a variável b:"))
c= float(input("Digite a variável c:"))

d = (b**2 - 4*a*c)

if d > 0:
  delta = math.sqrt(d)
   x1 = (-b + delta)/ (2*a)
   x2 = (-b - delta) / (2*a)	
   print ("as raízes da equação são", x1 ,"e", x2)
   
elif d==0:
  delta = math.sqrt(d)
  x = -b /(2*a)
  print ("a raiz desta equação é ", x)
 
elif d < 0:
   print ("esta equação não possui raízes reais")

