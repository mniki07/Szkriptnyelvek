#Állapítsuk meg azon 1000-nél kisebb számok összegét, 
#melyek 3-nak vagy 5-nek a többszörösei.

def main():
    answer=sum([(i) for i in range(1,1000) if int(i)%3==0 or int(i)%5==0]) #list comprehension segítségével megkeressük a számokat
    print(answer)

if __name__ == '__main__':
    main()
