#URL-ek tisztítása whitespace karakterektől

def tiszt(url):
    li = []
    li = url.split(':')
    eleje = li[0]
    vege = (li[1][2:]).strip()
    tiszta = eleje + ':' + vege
    return tiszta


def main():
    inp = input("Adja meg a szöveget: ")
    answer = tiszt(inp)
    print(answer)


if __name__ == '__main__':
    main()

