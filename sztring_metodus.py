#Válasszon ki egy tetszőleges sztring metódust
#s írjon egy kis szkriptet ami bemutatja ezen metódus működését.

# Megadja a beírt névben lévő első 'a' betű indexét (ha van benne)


def name_find():
    name=input('name: ')
    print(name.find('a'))


if __name__ == '__main__':
    name_find()

