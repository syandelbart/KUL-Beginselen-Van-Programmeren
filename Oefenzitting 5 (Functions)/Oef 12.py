def drawPyramid(height,symbol):
    n = 1
    string = ""
    while(n <= height):
        amount_symbols = (n * 2) - 1
        amount_spaces = (height * 2) - 1 - amount_symbols
        amount_spaces_each_side = int(amount_spaces / 2)

        for i in range((amount_spaces_each_side)):
            string += " "
        for i in range(amount_symbols):
            string += symbol
        for i in range((amount_spaces_each_side)):
            string += " "
        string += "\n"

        n += 1
    return string

def main():
    print(drawPyramid(7,"#"))
    print(drawPyramid(5,"*"))

main()