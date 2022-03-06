#Mennyi 2^1000 számjegyeinek az összege?


def ossz(num):
    osszeg=0
    for i in str(num):
        osszeg+=int(i)

    return osszeg


def main():
    n=2**1000
    print(ossz(n))


if __name__ == '__main__':
    main()

