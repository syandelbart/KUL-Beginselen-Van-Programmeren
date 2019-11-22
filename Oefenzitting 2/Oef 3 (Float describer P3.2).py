user_input = float(input("Input a floating-point number: "))

if user_input == 0:
    print_str = "zero."
elif user_input > 0:
    print_str = "positive number."
elif user_input < 0:
    print_str = "negative number."

if user_input < 1:
    print_str = "a small " + print_str
elif user_input > 1000000:
    print_str = "a large " + print_str



print("This number is", print_str)