#Írjunk egy függvényt a következő szignatúrával: valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
#A függvény egy olyan (akár üres) sztringgel térjen vissza, mely a "text"-ből 
#(első paraméter) csak azokat a karaktereket tartalmazza, melyek szerepelnek a "chars"-ban.

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"): #a fv-nek kell megadni egy szöveget, és opcionális paraméterként a karaktereket amiben keressük a szöveg betűit
    tart = ""
    for i in text:
        if i in chars:
            tart = tart + i
    return tart


def main():
    ans = valid("Barking!")
    print(ans)
    ans1 = valid("KL754", "0123456789")
    print(ans1)
    ans2 = valid("BEAN", "abcdefghijklmnopqrstuvwxyz")
    print(ans2)


if __name__ == '__main__':
    main()
