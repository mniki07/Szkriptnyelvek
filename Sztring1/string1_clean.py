






def donuts(count):
    if count<10:
        return(f"Fánkok száma: {count}")
    else:
        return("Fánkok száma: sok")



def both_ends(s):
    if len(s)<2:
        return("")
    else:
        return(s[:2]+s[-2:])



def fix_start(s):
    return(s[0]+s[1:].replace(s[0], '*'))



def mix_up(a, b):
    return(b[:2]+a[2:]+" "+a[:2]+b[2:])


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
    print('donuts') #ezzel most nem muszáj foglalkozni





if __name__ == '__main__':
    main()
