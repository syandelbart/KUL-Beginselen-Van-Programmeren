def sum(number):
    n = 0
    sum = 0
    while(n < number):
        sum += n
        n += 1
    return sum



def main():
    number = int(input("Geef getal tot waar geteld moet worden:"))
    print("De som van alle getallen 1 <= number is:", sum(number))

main()