#Írjon egy függvényt, mely kap egy N egész értéket. 
#A függvény visszatérési értéke a legkisebb olyan M >= N szám legyen,
#ahol M prím és palindróm is egyben.

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi = n ** 0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True


def primpal(numb: int) -> str:
    pp = 0
    wh = False
    while (wh == False):
        if is_prime(numb):
            numb = str(numb)
            if numb[:] == numb[::-1]:
                wh = True
                pp = numb
        numb = int(numb)
        numb += 1
    return pp


def main()->None:
    inp = input("Adjon meg egy számot! ")
    print(primpal(int(inp)))


if __name__ == '__main__':
    main()
