def primeNumbers(number):
    test_num = 2
    prime_array = []
    while(test_num <= number):
        divider = 2
        amount_dividers = 0
        while(divider < test_num and amount_dividers < 2):
            if(test_num % divider == 0):
                amount_dividers += 1
            divider += 1
        if(amount_dividers == 0): #by one and itself
            prime_array.append(test_num)

        test_num += 1

    return prime_array

def main():
    number = int(input("Give number to test whether is prime or not:"))
    print("Prime number(s) until given border:",primeNumbers(number))


main()