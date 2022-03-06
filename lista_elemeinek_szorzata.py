#Írjunk függvényt, mely kap egy egészeket tartalmazó listát 
#s visszaadja a listában lévő elemek szorzatát.

def product(numbers):
    prod = 1
    for e in numbers:
        prod *= e
    return prod


def main():
    li1 = [1, 2, 3, 4, 5]
    li2 = [10, 20, 30, 40, 50]
    li3 = []
    print(product(li1))
    print(product(li2))
    print(product(li3))


if __name__ == '__main__':
    main()
