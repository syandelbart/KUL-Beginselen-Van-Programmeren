user_input = int(input("Prime number?: "))
#PRE: user_input is een element van de positieve natuurlijke getallen
not_found = True
divider = 1
amount_dividers = 0
# INVARIANT: amount_dividers telt alle mogelijke delers tot divider, amount_dividers <= divider
while not_found and (divider < user_input):
    # INVARIANT EN not_found is false zolang priem niet gevonden, divider < user_input
    # dus: amount_dividers telt alle mogelijke delers tot divider, amount_dividers <= divider
    # EN divider < user_input
    if user_input % divider == 0:
        amount_dividers += 1
    #amount_dividers telt alle mogelijke delers tot divider, amount_dividers <= divider
    divider += 1
    #amount_dividers telt alle mogelijke delers tot divider-1, amount_dividers <= divider

if amount_dividers > 1 and user_input != 1:
    print("Geen priemgetal.")
else:
    print("Is een priemgetal.")

#POST: Het programma print "Geen priemgetal." als het geen priemgetal is, anders (als het wel
# een priemgetal is) print het "Is een priemgetal." uit.

# 4.1) VARIANT: user_input - divider
# 4.2) strikte ondergrens: user_input - user_input = 0
# 4.3) monotone daling: divider wordt elke iteratie opgeteld met 1 eenheid, dus user_input - divider
# wordt elke iteratie 1 eenheid kleiner
# 4.4) eindig aantal decrementen: iteratie start bij 0, en eindigt bij user_input want divider = user_input, dus is geldig