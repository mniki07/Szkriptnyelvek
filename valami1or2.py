# if inp == 'y' or inp == 'Y' or inp == 'yes': egyszerűsítése

import sys


def main():
    inp = input("Do you really want to quit [y/Y/yes]? ")
    #if inp == 'y' or inp == 'Y' or inp == 'yes':
    li = ["y", "yes", "Y"]
    if inp in li:
        print('bye')
        sys.exit(0)
    print('The show goes on...')


if __name__ == "__main__":
    main()