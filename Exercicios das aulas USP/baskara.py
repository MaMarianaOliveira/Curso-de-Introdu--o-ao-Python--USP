a = int (input("Digite a variável a:"))
b= int(input("Digite a variável b:"))
c= int(input("Digite a variável c:"))

delta = (b**2 - 4*a*c)

if delta < 0:
   print ("Essa raíz é imaginária!")

if delta > 0:
   print ("Esse cálculo tem 2 raízes")

if delta==0:
  print ("Esse cálculo tem 1 raíz")

