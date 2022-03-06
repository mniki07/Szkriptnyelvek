#Feladat: https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20160613a

def hatosl():
    pos_nums = []
    for num in range(1, 45):
        if 996300 % num == 0:
            pos_nums.append(num)

    for n1 in pos_nums:
        for n2 in pos_nums:
            for n3 in pos_nums:
                for n4 in pos_nums:
                    for n5 in pos_nums:
                        for n6 in pos_nums:
                            if n1 < n2 < n3 < n4 < n5 < n6:
                                if n1 + n2 + n3 + n4 + n5 + n6 == 90:
                                    if n1 * n2 * n3 * n4 * n5 * n6 == 996300:
                                        print(n1, n2, n3, n4, n5, n6)


def main():
    hatosl()


if __name__ == "__main__":
    main()
