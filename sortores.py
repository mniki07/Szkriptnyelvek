#Az alábbi kódrészlet 100 db random számjegyet állít elő s nyomtat ki egymás mellé
#Módosítsuk a kódot úgy, hogy egy sorba csak 10 számjegy kerüljön


import sys
import random as r

UPTO = 100


def main():
    n = 0
    for i in range(UPTO):
        print(r.randint(0, 9), end="")
        n+=1
        if n%10==0:
            print('\r')


if __name__ == '__main__':
    main()

