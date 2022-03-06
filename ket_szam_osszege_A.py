#Olvassunk be két egész számot s írjuk ki a két szám összegét.
#A két egész számot parancssori argumentumként adjuk meg. 
#Ha a felhasználó nem adja meg mindkét számot, akkor írjunk ki egy hibaüzenetet!


import sys


def hello(s1, s2):
    print(int(s1)+int(s2))


def main():
    if len(sys.argv)==3:
        szam1 = sys.argv[1]
        szam2 = sys.argv[2]
        hello(szam1, szam2)
    else:
        print("A bemenet száma nem megfelelő!")


if __name__ == "__main__":
    main()
