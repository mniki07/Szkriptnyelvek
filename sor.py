#Írjon egy osztályt, ami megvalósítja a sor adatszerkezetet.

class Sor:
    def __init__(self):
        self.data = []

    def betesz(self, value):
        self.data.append(value)

    def kivesz(self):
        if self.ures():
            None
        else:
            val = self.data[0]
            self.data.remove(self.data[0])
            return val

    def meret(self):
        return len(self.data)

    def ures(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.data[::-1])


def main():
    s = Sor()
    print(s)
    s.betesz(9)
    s.betesz(2)
    s.betesz(7)
    s.betesz(12)
    print(s)
    print(s.meret())
    print(s.ures())
    x = s.kivesz()
    print(x)
    print(s)
    s.kivesz()
    s.kivesz()
    s.kivesz()
    print(s.ures())
    x = s.kivesz()
    print(x)


if __name__ == '__main__':
    main()
