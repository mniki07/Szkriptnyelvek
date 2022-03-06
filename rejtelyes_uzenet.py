#TEXT dekódolása
#"K → M, O → Q, E → G"


TEXT = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""

ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z', 'A', 'B']
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z', 'a', 'b']
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


def main():
    TEXT2 = """"""
    for letter in TEXT:
        if letter in ABC:
            for x in nums:
                n = x
                if letter == ABC[x]:
                    TEXT2 += ABC[n + 2]

        if letter in abc:
            for x in nums:
                n = x
                if letter == abc[x]:
                    TEXT2 += abc[n + 2]
        if letter not in ABC and letter not in abc:
            TEXT2 += letter

    print(TEXT2)


if __name__ == '__main__':
    main()
