#Számítsuk ki a síkban két pont között a távolságot.

import math


def distance(p1, p2):
    ahossz=p2[0]-p1[0]
    bhossz=p2[1]-p1[1]
    tav=math.sqrt(ahossz*ahossz+bhossz*bhossz)
    return tav


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()