valor_intt = valor_itt1 = valor_itt2 = valor_itt3 = 1

def fizzbuzz(n):
    rest = n//5
    valor_itt = n % 5
    if valor_itt == 0 :
        print ("Buzz")
    elif n % 3 == 0 and  n % 5 == 0:
        print ("FizzBuzz")
    elif  n // 3 and  n % 3 == 0:
        print ("Fizz")
    else:
        print (n)
