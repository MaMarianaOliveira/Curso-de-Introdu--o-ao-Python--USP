valor_intt = valor_itt1 = valor_itt2 = valor_itt3 = 1

def fizzbuzz(n):
    rest = n//5
    valor_itt = n % 5
    if valor_itt == 0 :
        print ("Buzz")
    else:
        print (n)

def cinco_tres (m):
    valor_itt1 = m % 3
    valor_itt2 = m % 5
    if (valor_itt1 ==0) and (valor_itt2 == 0):
        print ("FizzBuzz")
    else:
        print (m)

def tres(j):
    rest = j // 3
    valor_itt3 = j % 3
    if valor_itt3 == 0:
        print ("Fizz")
    else:
        print (j)
