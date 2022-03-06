def main():
    f = open("string1.py", 'r')
    fm = open("string1_clean.py", 'w')
    for line in f:
        line = line.rstrip("\n")
        if not line.lstrip().startswith("#"):
            print(line, file=fm)
    # print(line, end="", file=fm)
    f.close()
    fm.close()


if __name__ == '__main__':
    main()
