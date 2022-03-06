#Feladat: https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20200415a

def my_function():
    f=open("hun-corpus.txt", "r", encoding="utf8")
    input_datas=f.readlines()
    datas=[]
    for input_line in input_datas:
        temp=input_line.split(",")
        datas.append(temp[0])

    key_letters=["j", "s", "u", "n"]

    results=[]
    for data in datas:
        order_of_occurence = []
        if "j" in data and "s" in data and "u" in data and "n" in data:
            order_of_occurence.append(data.find('j'))
            order_of_occurence.append(data.find('s'))
            order_of_occurence.append(data.find('u'))
            order_of_occurence.append(data.find('n'))
            if order_of_occurence==sorted(order_of_occurence):
                results.append(data)

    if len(results)==0:
        print("Nincs ilyen magyar szavunk")
    else:
        print("A megfelelő magyar szó:")
        for item in results:
            print(item)


def main():
    my_function()



if __name__ == "__main__":
    main()