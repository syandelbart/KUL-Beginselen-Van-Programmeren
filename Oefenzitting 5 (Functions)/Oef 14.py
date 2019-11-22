def sum_numbers(input):
    sum = 0
    input_string = str(input)
    for i in range(len(input_string)):
        sum += int(input_string[i])
    return sum

def get_check_num(number):
    return 10 - (number % 10)


def encode_num(num):
    if(num == 1):
        return ":::||"
    elif(num == 2):
        return "::|:|"
    elif(num == 3):
        return "::||:"
    elif(num == 4):
        return ":|::|"
    elif(num == 5):
        return ":|:|:"
    elif(num == 6):
        return ":||::"
    elif(num == 7):
        return "|:::|"
    elif(num == 8):
        return "|::|:"
    elif(num == 9):
        return "|:|::"
    elif(num == 0):
        return "||:::"
    else:
        return -1

def encode_string(input):
    string = ""
    input_string = str(input)
    input_string += str(get_check_num(sum_numbers(input)))
    print(input_string)
    for i in range(len(input_string)):
        string += encode_num(int(input_string[i]))
        string += "  "
    return string

def main():
    number = int(input("Give number:"))
    print(get_check_num(sum_numbers(number)))
    print(encode_string(number))

main()