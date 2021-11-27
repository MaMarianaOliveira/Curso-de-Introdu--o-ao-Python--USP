def maior_primo(x):
    for k in range(x, 1, -1):
        if primo(k):
            return k


def primo(y):
    n = 1
    cont = 0
    while n <= y:
        if y % n == 0:
            cont += 1
        n += 1
        if cont > 2:
            return False
    return True
