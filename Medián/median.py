#adott számoknak egy listája. Határozzuk meg a medián értékét.

def med(li):
    rend=sorted(li)
    if len(rend)%2==1:
        median=rend[int(len(rend)/2)]
    if len(rend)%2==0:
        median=(rend[int(len(rend)/2)-1]+rend[int(len(rend)/2)])/2
    return median


def main():
    li1=[1,2,3,4,5]
    li2=[3,1,2,5,3]
    li3=[1,300,2,200,1]
    li4=[3,6,20,99,10,15]
    print(med(li1))
    print(med(li2))
    print(med(li3))
    print(med(li4))



if __name__ == '__main__':
    main()

