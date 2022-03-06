#Írjunk függvényt, mely egy sztringről eldönti, hogy palindróm-e.
#Rekurzív módszer.

def palindromrek(szo):
    if len(szo) == 0:
        return szo
    else:
        return palindromrek(szo[1:]) +szo[0]


def main():
    bemenet = input('Adjon meg 1 szót: ')
    szorek = palindromrek(bemenet)
    if bemenet==szorek:
        print("A beírt szó palindróm")
    else:
       print("A beírt szó nem palindróm")




if __name__ == '__main__':
    main()
