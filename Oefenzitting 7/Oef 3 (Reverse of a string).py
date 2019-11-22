def reverse(string):
    if(len(string) == 0):
        return ""
    elif(len(string) == 1):
        return string
    else:
        print(string)
        return string[-1] + reverse(string[1:len(string)-1]) + string[0]

def main():
    string = str(input("Geef string:"))
    print(reverse(string))

main()