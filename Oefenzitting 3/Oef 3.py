not_quit = True
user_input = ""
counter = 0
sum = 0
while not_quit:
    user_input = int(input("Number: "))
    if(user_input != 0):
        if (counter % 2 == 0):
            sum += user_input
        else:
            sum -= user_input
        counter += 1
    else:
        not_quit = False
print(sum)