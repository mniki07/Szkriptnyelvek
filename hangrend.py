#Döntsük el egy magyar szóról,
#hogy milyen hangrendű (mély, magas, vegyes, vagy semmilyen hangrendű).

MELY = ['a', 'á', 'o', 'ó', 'u', 'ú']
MAGAS = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']


def rend(word):
    mely = 0
    magas = 0
    for n in word:
        if n in MAGAS:
            magas += 1
        if n in MELY:
            mely += 1
    if mely == 0 and magas != 0:
        return ("magas")
    if mely != 0 and magas == 0:
        return ("mély")
    if mely != 0 and magas != 0:
        return ("vegyes")
    if mely == 0 and magas == 0:
        return ("semmilyen")


def main():
    szo = input("Írjon be egy szót: ")
    valasz = rend(szo)
    if valasz == "magas":
        print("magas hangrendű")
    if valasz == "mély":
        print("mély hangrendű")
    if valasz == "vegyes":
        print("vegyes hangrendű")
    if valasz == "semmilyen":
        print("semmmilyen")


if __name__ == '__main__':
    main()

