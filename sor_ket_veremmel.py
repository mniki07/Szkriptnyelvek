#Sor adatszerkezet megvalósítása két veremmel

class Verem:
    def __init__(self):
        self.data = []

    def betesz(self, value):
        self.data.append(value)

    def kivesz(self):
        if self.ures():
            return None
        else:
            return self.data.pop()

    def meret(self):
        return len(self.data)

    def ures(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.data)


class MyQueue:
    def __init__(self):
        self.v = Verem()

    def append(self, value):
        self.v.betesz(value)

    def is_empty(self):
        if self.v.meret() == 0:
            return True
        else:
            return False

    def size(self):
        return self.v.meret()

    def popleft(self):
        data = Verem()
        size = self.size() - 1
        while size > 0:
            data.betesz(self.v.kivesz())
            size -= 1
        temp = self.v.kivesz()
        self.v = data
        return temp

    def __str__(self):
        data = []
        i = self.v.meret() - 1
        while i > -1:
            data.append(self.v.kivesz())
            i -= 1
        i = len(data) - 1
        while i > -1:
            self.v.betesz(data[i])
            i -= 1
        return str(data)


def main():
    q = MyQueue()
    print(q)
    print(q.is_empty())
    q.append(4)
    q.append(6)
    q.append(8)
    print(q)
    print(q.size())
    print(q.is_empty())
    x = q.popleft()
    print(x)
    print(q)
    q.popleft()
    q.popleft()
    x = q.popleft()
    print(x)


if __name__ == '__main__':
    main()
