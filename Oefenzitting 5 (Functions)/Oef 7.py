def isPerfectNumber(number):
    divider = 1
    sum = 0
    while(divider < number):
        if(number % divider == 0):
            sum += divider
        divider += 1
    if(sum == number):
        return True
    else:
        return False


def main():
    number = int(input("Give number to test whether is prime or not:"))
    if(isPerfectNumber(number)):
        print("The number",number,"is a perfect number.")
    else:
        print("The number",number,"is not a perfect number.")

    print("Next exercise:")
    for i in range(10000):
        if(isPerfectNumber(i)):

            print(i,"is a perfect number.")


main()