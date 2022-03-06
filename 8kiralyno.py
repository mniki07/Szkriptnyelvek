#egy sakktáblán helyezzünk el 8 királynőt úgy, hogy ne üssék egymást.
#írjunk egy olyan eljárást, mely kap egy 8 elemű listát, s ez alapján megrajzolja a sakktáblát.

def rajz(li):
    print("+-----------------+")
    for i in li:
        if i == 7:
            print("| Q . . . . . . . |")
        if i == 6:
            print("| . Q . . . . . . |")
        if i == 5:
            print("| . . Q . . . . . |")
        if i == 4:
            print("| . . . Q . . . . |")
        if i == 3:
            print("| . . . . Q . . . |")
        if i == 2:
            print("| . . . . . Q . . |")
        if i == 1:
            print("| . . . . . . Q . |")
        if i == 0:
            print("| . . . . . . . Q |")
    print("+-----------------+")


def main():
    li1 = [0, 4, 7, 5, 2, 6, 1, 3]
    rajz(li1)
    li2 = [7, 3, 0, 2, 5, 1, 6, 4]
    rajz(li2)


if __name__ == '__main__':
    main()
