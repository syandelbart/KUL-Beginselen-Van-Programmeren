def fibo(number):
    num1 = 1
    num2 = 1
    num3 = 0 #taking value to pass it along
    n = 2
    while(n < number):
        num3 = num1
        num1 = num1 + num2
        num2 = num3
        n += 1
    return num1



def main():
    number = int(input("Geef nummer in voor aantal keer dat fibonnaci moet uitgevoerd worden:"))
    print("Het",number,"de getal in de Fibonacci rij is:",fibo(number))

main()