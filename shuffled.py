#Készítsünk egy shuffled nevű függvényt, 
#mely visszatér az összekevert elemeket tartalmazó listával

import random


def shuffled(li):
    copy = li[:]  # li.copy()
    random.shuffle(copy)
    return copy


def main():
    li = [1, 2, 3, 4, 5]
    uj = shuffled(li)
    print(uj)
    print(li)

if __name__ == '__main__':
    main()
