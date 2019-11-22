def factors(n):
    if n > 1:
        found = False
        divider = 2
        while(divider < n and not found):
            if(n % divider == 0):
                found = True
            else:
                divider += 1

        return [divider] + factors(n // divider)
    else:
        return []



def main():
    get = int(input("Geef getal waarvan factors:"))
    print(factors(get))

main()