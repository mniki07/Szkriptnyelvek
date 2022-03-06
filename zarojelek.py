#egy kifejezésről döntsük el a zárójelek alapján, hogy helyes-e vagy sem

def brackets(inp):
    openround = 0
    closeround = 0
    opensquare = 0
    closesquare = 0
    opencurly = 0
    closecurly = 0
    open = []
    close = []

    for i in inp:
        if i in ('(', '[', '{'):
            open.append(i)
        if i in (')', ']', '}'):
            close.append(i)

    for i in inp:
        if i == '(':
            openround += 1
        if i == ')':
            closeround += 1
        if i == '[':
            opensquare += 1
        if i == ']':
            closesquare += 1
        if i == '{':
            opencurly += 1
        if i == '}':
            closecurly += 1

    if openround == closeround and opensquare == closesquare and opencurly == closecurly:
        close = close[::-1]
        for i in range(len(open)):
            if (open[i] == '(' and close[i] == ')') or (open[i] == '[' and close[i] == ']') or (
                    open[i] == '{' and close[i] == '}'):
                return True
    else:
        return False


def main():
    ans1 = brackets("((5+3)*2+1)")
    if ans1:
        print("True")
    else:
        print("False")

    ans2 = brackets("{[(3+1)+2]+}")
    if ans2:
        print("True")
    else:
        print("False")

    ans3 = brackets("(3+{1-1)}")
    if ans3:
        print("True")
    else:
        print("False")

    ans4 = brackets("[1+1]+(2*2)-{3/3}")
    if ans4:
        print("True")
    else:
        print("False")

    ans5 = brackets("(({[(((1)-2)+3)-3]/3}-3)")
    if ans5:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
