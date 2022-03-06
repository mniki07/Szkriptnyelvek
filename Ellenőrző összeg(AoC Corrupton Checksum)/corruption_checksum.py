#Minden egyes sorban állapítsuk meg a legnagyobb és a legkisebb szám különbségét.
# Az ellenőrző összeg ezen soronkénti különbségek összege lesz.

def main():
    f = open("day02.txt", "r")
    sorkul = []
    for line in f:
        line2 = line.split()
        maximum = int(max(line2))
        minimum = int(min(line2))
        sorkul.append(maximum - minimum)
    print(sum(sorkul))
    f.close()


if __name__ == '__main__':
    main()
