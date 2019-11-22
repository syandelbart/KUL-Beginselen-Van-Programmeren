def factorial(number):
    sum = 1
    n = 1
    while(n <= number):
        sum *= n
        n += 1
    return sum

def main():
    number = int(input("Give number:"))
    print("Factorial:",factorial(number))


main()