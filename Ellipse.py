#Ellipszis osztály megírása

import math


class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b * math.pi

    def __bool__(self):
        return self.area() > 0

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __str__(self):
        return "Ellipse({a}, {b})".format(a=self.a, b=self.b)


def main():
    e = Ellipse(2, 1)
    e1 = Ellipse(4, 3)
    print(e > e1)
    print(e < e1)
    print(e == e1)
    print(e.area())
    if e1:
        print("e1 igazak számít")
    else:
        print("e1 hamisnak számít")
    print(e)


if __name__ == '__main__':
    main()
