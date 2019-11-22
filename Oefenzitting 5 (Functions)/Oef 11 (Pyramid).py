def drawPyramid(height,symbol):
    n = 1
    while(n <= height):
        amount_symbols = (n * 2) - 1
        amount_spaces = (height * 2) - 1 - amount_symbols
        amount_spaces_each_side = int(amount_spaces / 2)

        for i in range((amount_spaces_each_side)):
            print(" ",end="")
        for i in range(amount_symbols):
            print(symbol,end="")
        for i in range((amount_spaces_each_side)):
            print(" ",end="")
        print()

        n += 1

def main():
    drawPyramid(10,"#")
    drawPyramid(5,"*")

main()