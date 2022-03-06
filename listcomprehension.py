#Feladat: https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120818d

def print_hi():
    print('1.feladat')
    inp=['auto', 'villamos', 'metro']
    result=[s.upper()+'!' for s in inp]
    for i in result:
        print(i)
    print("------------------------------")
    print('2.feladat')
    nevek=['aladar', 'bela', 'cecil']
    result1=[s.capitalize() for s in nevek]
    for i in result1:
        print(i)
    print("------------------------------")
    print('3.feladat')
    result2=[0 for i in range(10)]
    for i in result2:
        print(i)
    print("------------------------------")
    print('4.feladat')
    inp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result3=[i+i for i in inp]
    for i in result3:
        print(i)
    print("------------------------------")
    print('5.feladat')
    inp=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    result4=[int(i) for i in inp]
    for i in result4:
        print(i)
    print("------------------------------")
    print('6.feladat')
    inp="1234567"
    result5 = [i for i in inp]
    for i in result5:
        print(i)
    print("------------------------------")
    print('7.feladat')
    s="The quick brown fox jumps over the lazy dog"
    result6=[len(szo) for szo in s.split()]
    for i in result6:
        print(i)
    print("------------------------------")
    print('8.feladat')
    inp="python is an awesome language"
    result7=[i[0] for i in inp.split()]
    for i in result7:
        print(i)
    print("------------------------------")
    print('9.feladat')
    inp='The quick brown fox jumps over the lazy dog'
    result8=[(i,len(i)) for i in inp.split()]
    for i in result8:
        print(i)
    print("------------------------------")
    print('10.feladat')
    result9=[i for i in range(10) if i%2==0]
    for i in result9:
        print(i)
    print("------------------------------")
    print('11.feladat')
    result10=[i*i for i in range(20) if i*i%2==0]
    for i in result10:
        print(i)
    print("------------------------------")
    print('12.feladat')
    result11 = [i * i for i in range(20) if (i * i)%10 == 4]
    for i in result11:
        print(i)
    print("------------------------------")




if __name__ == '__main__':
    print_hi()

