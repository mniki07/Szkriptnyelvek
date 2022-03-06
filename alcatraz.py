#Feladat: https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815k

def open_door():
    n = 600
    li = []
    for i in range(0, n):
        li.append(0)

    th = 1
    for round in range(1, n + 1):
        for door_number in range(0, n):
            if (door_number + 1) % th == 0:
                if li[door_number] == 0:
                    li[door_number] = 1
                else:
                    li[door_number] = 0
        th += 1

    for door_number in range(len(li)):
        if li[door_number] == 0:
            print(str(door_number + 1) + ",", end=" ")


def main():
    open_door()


if __name__ == "__main__":
    main()
