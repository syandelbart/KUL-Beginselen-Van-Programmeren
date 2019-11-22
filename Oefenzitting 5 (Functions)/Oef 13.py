def sum_numbers(input):
    sum = 0
    input_string = str(input)
    for i in range(len(input_string)):
        sum += int(input_string[i])
    return sum

def get_check_num(number):
    return 10 - (number % 10)


def main():
    number = int(input("Give number:"))
    print(get_check_num(sum_numbers(number)))

main()