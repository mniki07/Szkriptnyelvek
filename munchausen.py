#Keressük meg az összes Münchausen-számot! A keresést 0-ról indítsuk. 
#Egy kis segítség: a legnagyobb Münchausen-szám 440 milliónál kisebb.

def munchausen():
    nums = [i ** i for i in range(10)] #a számok hatványának kiszámítása
    nums[0] = 0

    for number in range(440000000):
        strnumber = str(number)
        sum = 0
        for i in strnumber:
            sum += nums[int(i)] #az összeg létrehozás
        if sum == number: #szám hasonlítása az összeghez
            print(sum)


def main():
    munchausen()


if __name__ == '__main__':
    import time
    #futási idő számítása
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
