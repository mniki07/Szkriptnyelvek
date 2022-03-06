#Számoljuk ki azon egy milliónál kisebb pozitív számok összegét, melyek mind a 10-es, 
#mind a 2-es számrendszerben palindróm tulajdonsággal rendelkeznek.

def dectobin(n: int) -> str:
    bi = ""
    while n >= 1:
        if n % 2 == 1:
            bi = bi + '1'
            n = ((n - 1) / 2)
        else:
            bi = bi + '0'
            n = (n / 2)
    return bi[::-1]


def pal(n: int) -> bool:
    numb = str(n)
    if numb[:] == numb[::-1]:
        return True
    else:
        return False


def main() -> None:
    ossz = 0
    for i in range(1, 1000001):
        if pal(int(i)):
            number = dectobin(i)
            if number.startswith('1') and pal(number):
                ossz = ossz + i
    print(ossz)


if __name__ == '__main__':
    main()
