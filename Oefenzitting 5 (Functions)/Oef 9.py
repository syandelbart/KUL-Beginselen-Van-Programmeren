def factorial(number):
    sum = 1
    n = 1
    while(n <= number):
        sum *= n
        n += 1
    return sum

def estimateExp(power):
    n = 0
    grens = 1000
    sum = 0
    while(n < grens):
        sum += (power ** n) / factorial(n)
        n += 1
    return sum


def main():
    number = int(input("Give number:"))
    print("Estimate of e^x:",estimateExp(number))


main()