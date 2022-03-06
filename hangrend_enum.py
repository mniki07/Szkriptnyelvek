#Döntsük el egy magyar szóról,
#hogy milyen hangrendű (mély, magas, vegyes, vagy semmilyen hangrendű).
#Enum használatával

from enum import Enum


class Mely(Enum):
    a = "a"
    á = "á"
    o = "o"
    ó = "ó"
    u = "u"
    ú = "ú"


class Magas(Enum):
    e = "e"
    é = "é"
    i = "i"
    í = "í"
    ö = "ö"
    ő = "ő"
    ü = "ü"
    ű = "ű"


class hangrend_fajt(Enum):
    res1 = "magas"
    res2 = "mély"
    res3 = "vegyes"
    res4 = "semmilyen"


def hangrend(word):
    magas = False
    mely = False
    for letter in word:
        for enum in Magas:
            if str(letter) == enum.value:
                magas = True
        for enum in Mely:
            if str(letter) == enum.value:
                mely = True

    if mely == False and magas == False:
        return hangrend_fajt.res4.value
    if mely == True and magas == True:
        return hangrend_fajt.res3.value
    if mely == True and magas == False:
        return hangrend_fajt.res2.value
    if mely == False and magas == True:
        return hangrend_fajt.res1.value


def main():
    word = input("Kérek egy szót:")
    print("A megadott szó " + hangrend(word) + " hangrendű")


if __name__ == '__main__':
    main()
