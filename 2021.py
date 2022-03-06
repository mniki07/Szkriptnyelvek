#Írjon egy szkriptet, ami kiírja a 2021-et úgy, 
#hogy a forráskódban egyetlen számjegyet sem használ!

def main(): #az ASCII kódokat használja a számok helyet
    A = 'Z'
    B = 'F'
    C = 'E'
    print(ord(A) - ord(B), end="")
    print(ord(A) - ord(C), end="")


if __name__ == '__main__':
    main()
