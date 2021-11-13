        #Ex1

def sum_int(*args):
    s = 0
    for i in args:
        if type(i) == int or type(i) == float:
            s = s + i
    return s



        #Ex2

def n_average(n: int, par=False, impar=False) -> int:

    if par and impar:
        par = False
        impar = False
    if n <= 0:
        return 0
    if par:
        if n % 2 != 0:
            n -= 1
        return n + n_average(n - 2, par=True)
    if impar:
        if n % 2 == 0:
            n -= 1
        return n + n_average(n - 2, impar=True)
    return n + n_average(n - 1)


        #Ex3

def read_integers() -> int:

    a = input("Insert something:")
    try:
        return int(a)
    except ValueError:
        return 0


