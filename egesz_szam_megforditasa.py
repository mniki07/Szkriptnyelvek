#Írjunk függvényt, mely kap egy pozitív egész számot,
#s visszatérési értékként a szám fordítottját adja vissza mint egész számot.

def ford(szam):
    seged_ford=str(szam)
    forditott=int(seged_ford[::-1])
    return(forditott)


def main():
    number=int(input('Szám: '))
    valasz=ford(number)
    print(valasz)


if __name__ == '__main__':
    main()
