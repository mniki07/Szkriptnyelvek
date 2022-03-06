#Feladat: https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20180312a

def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord('a'),ord('z')+1))

    for t in zip(chars,codes):
        print(t)


if __name__ == '__main__':
    main()
