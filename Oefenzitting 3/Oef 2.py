'first time unskippable --> actually it is skippable since if statement already blocks
not_quit = True
while not_quit:
    user_input = str(input("Celsius: "))
    if user_input != "q":
        num = int(user_input)
        print("Fahrenheit:", num * 9 / 5 + 32)
    else:
        not_quit = False


user_input = str(input("Celsius"))
while user_input != "q":
    num = int(user_input)
    print("Fahrenheit:", num * 9 / 5 + 32)
    user_input = str(input("Celsius: "))
