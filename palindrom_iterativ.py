#Írjunk függvényt, mely egy sztringről eldönti, hogy palindróm-e.
#Iteratív módszer. A sztringről nem készíthetünk másolatot.

def palindromiter(word):
    n = 0
    for e in word:
        n -= 1
        if e != word[n]:
            return False
    return True


def main():
    inp = input("Írjon be egy szót: ")
    if palindromiter(inp):
        print("A beírt szó palindróm")
    else:
        print("A beírt szó nem palindróm")


if __name__ == '__main__':
    main()
