#Vagyis a program interaktív módon kérje be a nevünket.
#A nevünk előtt és után hagyjunk szóközöket.A program üdvözöljön minket

def print_hi():
    name = input('name: ')
    print('Hello '+name.strip()+" !")


if __name__ == '__main__':
    print_hi()

