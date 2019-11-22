user_input = int(input("Number(s) to rotate: "))
length_not_found = True
divider = 1
length = 0
while length_not_found:
    length += 1
    if user_input / divider < 10:
        length_not_found = False
    divider *= 10


length_not_found = True
divider = 1
counter = 0
while length_not_found:
    counter += 1
    divider *= 10
    print(int((user_input % divider) / (divider / 10)),end="")
    if counter == length:
        length_not_found = False