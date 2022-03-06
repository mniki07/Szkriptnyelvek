#Írjunk függvényt, mely egy sztringről eldönti, hogy palindróm-e.
#triviális megoldás

def palindromtriv(szo):
    if szo[:]==szo[::-1]:
        return True
    else:
        return False


def main():
    bemenet=input('Adjon meg 1 szót: ')
    palindromtriv(bemenet)


if __name__ == '__main__':
    main()

