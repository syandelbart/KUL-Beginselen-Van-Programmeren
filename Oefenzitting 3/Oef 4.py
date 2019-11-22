#user_input = int(input("Prime number?: "))
#not_found = True
#divider = 1
#amount_dividers = 0
#while not_found and not (divider >= user_input):
#    if user_input % divider == 0:
#        amount_dividers += 1
#   divider += 1
#
#if amount_dividers > 1 and user_input != 1:
#    print("Geen priemgetal.")
#else:
#    print("Is een priemgetal.")


number_until = int(input("Until which number to test prime?: "))
for i in range(1,number_until + 1):
    not_found = True
    divider = 1
    amount_dividers = 0
    while not_found and not (divider >= i):
        if i % divider == 0:
            amount_dividers += 1
        divider += 1

    if (amount_dividers == 1 and i != 1) and i != number_until:
        print(i, end=" ")
    elif i == number_until:
        if (amount_dividers == 1 and i != 1) and i != number_until:
            print("(" + str(number_until) + " is also a prime number)")
        else:
            print("(" + str(number_until) + " is not a prime number)")


