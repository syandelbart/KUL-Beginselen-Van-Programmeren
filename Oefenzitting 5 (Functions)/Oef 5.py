def isPrime(number):
    divider = 2
    amount_dividers = 0
    while(divider < number and amount_dividers < 2):
        if(number % divider == 0):
            amount_dividers += 1
        divider += 1
    if(amount_dividers == 0): #by one and itself
        return True
    else:
        return False

def main():
    number = int(input("Give number to test whether is prime or not:"))
    if(isPrime(number)):
        print("The number",number,"is a prime number.")
    else:
        print("The number",number,"is not a prime number.")


main()