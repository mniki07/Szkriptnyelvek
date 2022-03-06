#Bináris átalakítása

def bintodec(inp):
    inp = inp.split()
    out = ""
    for letter in inp:
        dec = 0
        letter = letter[::-1]
        lenght = len(letter)
        for i in range(0, lenght):
            dec += int(letter[i]) * 2 ** i
        out += chr(dec)
    return out


def main():
    ans = bintodec("01111001 01101111 01110101 01110100 01110101 00101110 01100010 01100101 00101111 01100100 01010001 01110111 00110100 01110111 00111001 01010111 01100111 01011000 01100011 01010001 ")
    print(ans)


if __name__ == '__main__':
    main()
