valor_intt = valor_itt1 = valor_itt2 = valor_itt3 = 1

def fizzbuzz(n):
    
    if n % 3 == 0 and  n % 5 == 0:
        return ("FizzBuzz")
    elif n % 5 == 0 :
        return ("Buzz")
    elif  n % 3 == 0:
        return ("Fizz")
    else:
        return (n)
