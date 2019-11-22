s = str(input("Input word: "))
# PRE: s moet een string zijn
amt = 0
len_string = len(s)
counter = 0
# INVARIANT: amt telt alle hoofdletters t.e.m. counter, amt <= len_string
while(counter < len_string):
    # INVARIANT EN counter < len_string
    # dus: amt telt alle hoofdletters t.e.m. counter, amt <= len_string EN counter < len_string
    if s[counter].isupper():
        amt+=1
    # amt telt alle hoofdletters t.e.m. counter EN counter < len_string
    counter += 1
    # amt telt alle hoofdletters t.e.m. counter-1 EN counter < len_string
    # DUS INVARIANT IS GELDIG

# POST: amt bevat een positief geheel getal dat staat voor het aantal hoofdletters
# in de ingegeven tekstwaarde

# 4.1) VARIANT: len_string - counter
# 4.2) strikte ondergrens: len_string - len_string = 0
# 4.3) monotone daling: counter wordt elke iteratie opgetelt --> len_string - counter daalt met 1 eenheid per iteratie
# 4.4) eindig aantal decrementen: iteratie start bij 0, en eindigt bij bovengrens len_string want dan is de counter = len_string
