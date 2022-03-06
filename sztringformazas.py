#format bemutatása

def main():
    print("{:.2f}".format(3.154875))
    print("{:.2f}".format(3))
    print("{:,}".format(10000000))
    print("{:10d}".format(500))
    s1 = "Az {} nem esik messze a {}.".format("alma", "fájától")
    print(s1)


if __name__ == '__main__':
    main()
