def fibo(number):
    num1 = 1
    num2 = 1
    num3 = 0 #taking value to pass it along
    n = 2

    if(number <= 2):
        return "1&2"

    while(num1 < number):
        num3 = num1
        num1 = num1 + num2
        num2 = num3
        n += 1
        if(num1 == number):
            return n


    return -1



def main():
    number = int(input("Geef nummer in voor hoeveelste element in Fibonacci:"))
    print("Het getal", number, "is het", fibo(number), "ste element in Fibonacci.")

main()