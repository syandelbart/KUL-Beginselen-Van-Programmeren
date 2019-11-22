import math
user_input = int(input())
while user_input < 0:
    user_input = int(input())
square_root_undivided = round(int(math.sqrt(user_input)))
total_by_square_root = square_root_undivided ** 2
remainder = user_input - total_by_square_root
if remainder == 0:
    added_value = 0
elif (remainder <= square_root_undivided):
    added_value = 2
else:
    added_value = 4
total = square_root_undivided * 2 + square_root_undivided * 2 + added_value
print(int(total))
