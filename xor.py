#Adott két változó, s döntsük el, hogy teljesül-e az, hogy az egyik igazként 
#míg a másik hamisként értékelődik ki. 
#Ez tulajdonképpen egy XOR művelet (kizáró vagy)


def xor(valt1, valt2):
    if bool(valt1) == True and bool(valt2) == False:
        return (True)
    if bool(valt1) == False and bool(valt2) == True:
        return (True)
    if bool(valt1) == False and bool(valt2) == False:
        return (False)
    if bool(valt1) == True and bool(valt2) == True:
        return (False)


def main():
    str1 = "python"
    str2 = None
    valasz = xor(str1, str2)
    print(valasz)
    
    str3 = None
    str4 = "python"
    valasz = xor(str3, str4)
    print(valasz)
    
    str5 = None
    str6 = None
    valasz = xor(str5, str6)
    print(valasz)
    
    str7 = "python"
    str8 = "python"
    valasz = xor(str7, str8)
    print(valasz)


if __name__ == '__main__':
    main()
