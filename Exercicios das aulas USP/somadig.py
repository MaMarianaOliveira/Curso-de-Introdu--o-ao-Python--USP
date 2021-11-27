n = int(input("Digito o número á ser somado : "))  
     
soma = 0

while n > 0:
   resto = n % 10
   n =  n // 10
   soma = soma + resto


print (soma)