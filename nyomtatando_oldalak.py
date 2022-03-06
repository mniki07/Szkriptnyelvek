#Ha egy dokumentum bizonyos oldalait szeretnénk kinyomtatni, 
#akkor ezt a következőképpen szoktuk megadni:1-4,7,9,11-15
#Írjunk egy olyan szkriptet, ami az oldalakat a fent megadott módon kéri be, 
#majd egy listában visszaadja az egyes nyomtatandó oldalakat.

from typing import List

def nyomt(line:str) -> List[str]:
    li = line.split(",")
    pages = []
    for i in li:
        if len(i) > 2:
            li2 = i.split("-")
            for page in range(int(li2[0]), int(li2[1]) + 1):
                pages.append(page)
        else:
            pages.append(int(i))
    return pages


def main()->None:
    inp = input("Adja meg az oldalakat!")
    print(nyomt(inp))


if __name__ == '__main__':
    main()
