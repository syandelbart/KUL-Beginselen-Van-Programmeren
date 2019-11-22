def factorial(number):
    sum = 1
    n = 1
    while(n <= number):
        sum *= n
        n += 1
    return sum

def comb(n,k):
    return factorial(n) / (factorial(k) * factorial(k-n))



def main():
    number1 = int(input("Give number 1 (n):"))
    number2 = int(input("Give number 2 (k):"))
    print("Combination set:",comb(number1,number2) / comb(number2,number2))


main()