#Gömb osztály megírása

import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def vol(self):
        return (4 * self.radius ** 3 * math.pi) / 3

    def __bool__(self):
        return self.vol() > 0

    def __lt__(self, other):
        return self.vol() < other.vol()

    def __le__(self, other):
        return self.vol() <= other.vol()

    def __gt__(self, other):
        return self.vol() > other.vol()

    def __ge__(self, other):
        return self.vol() >= other.vol()

    def __eq__(self, other):
        return self.vol() == other.vol()

    def __str__(self):
        return "Sphere({r})".format(r=self.radius)


def main():
    r1 = Sphere(2)
    r2 = Sphere(3)
    r3 = Sphere(2)
    if r1:
        print(r1.vol())
    else:
        print("negatív térfogat")
    print(r1 < r2)
    print(r1 <= r3)
    print(r1 > r2)
    print(r1 >= r3)
    print(r1 == r3)
    print(r1)


if __name__ == '__main__':
    main()
