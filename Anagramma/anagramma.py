#Írjunk egy függvényt, amely kap két sztringet, s eldönti, 
#hogy a második szó az első szó anagrammája-e vagy sem.

def normalize(string):
    norm1 = string.split()
    norm = ("".join(norm1)).lower()
    return norm


def anagramma(word1, word2):
    if sorted(normalize(word1)) == sorted(normalize(word2)):
        return True
    else:
        return False


def anagramma1(word1, word2):
    n = 0
    normword1 = sorted(normalize(word1))
    normword2 = sorted(normalize(word2))
    for i in range(len(normword1)):
        for i2 in range(len(normword2)):
            if i == i2:
                n += 1
    if len(normword1) == len(normword2) == n:
        return True
    else:
        return False


def main():
    ans = anagramma("listen", "silent")
    if ans == True:
        print("Anagramma")
    else:
        print("Nem anagramma")
    ans = anagramma1("dormitory", "dirty room")
    if ans == True:
        print("Anagramma1")
    else:
        print("Nem anagramma1")


if __name__ == '__main__':
    main()
