def power(x,n):
    if(n == 0):
        return 1
    else:
        return x * power(x,n-1)



def main():
    get = int(input("Geef getal waarvan power:"))
    pow = int(input("Geef power van getal:"))
    print(power(get,pow))

main()