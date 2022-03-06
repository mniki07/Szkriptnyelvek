#Írjunk egy függvényt, mely paraméterként megkapja egy gyémánt magasságát. 
#A függvény ezek után rajzolja ki a gyémántot.

from Tools.demo.spreadsheet import center


def epit(x):
    if int(x)%2:
        txt = "*"
        number = range(int(x) + 2, 1, -2)
        for n in number:
            print(txt.center(int(x)))
            txt = txt + "**"
        number=range(int(x)-2,0,-2)
        for n in number:
            txt1=n*'*'
            print(txt1.center(int(x)))
    else:
        print("Páros magasság esetén, nem lehet gyémántot kirajzolni")


def main():
    nums = input("Szám: ")
    epit(nums)


if __name__ == '__main__':
    main()
