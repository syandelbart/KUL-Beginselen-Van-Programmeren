def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n-1)


def main():
    get = int(input("Geef getal voor factorial:"))
    print(factorial(getal))


main()