def fibo(ondergrens,bovengrens):
    num1 = 1
    num2 = 1
    num3 = 0 #taking value to pass it along
    som = 0
    n = 2
    while(n < bovengrens):
        num3 = num1
        num1 = num1 + num2
        num2 = num3
        n += 1
        if(n >= ondergrens and n <= bovengrens):
            som += num1


    return som



def main():
    ondergrens = int(input("Ondergrens fibonacci:"))
    bovengrens = int(input("Bovengrens fibonacci:"))
    print("Vanaf getal",ondergrens,"tot",bovengrens,"is heeft als som", fibo(ondergrens,bovengrens))

main()