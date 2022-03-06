#Számítsuk ki az első száz természetes szám összegének a négyzete 
#és az első száz természetes szám négyzetösszege közti különbséget!

def main():
    numbers=range(101)
    negyzetosszeg=0
    for n in numbers:
        negyzetosszeg=negyzetosszeg+n*n
    osszeg=0
    for n in numbers:
        osszeg=osszeg+n
    negyzet=osszeg*osszeg
    kulonbseg=negyzet-negyzetosszeg
    print(kulonbseg)


if __name__ == '__main__':
    main()

