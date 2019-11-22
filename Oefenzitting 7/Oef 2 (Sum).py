def sum(list):
    if(len(list) == 0):
        return 0
    else:
        return list[0] + sum(list[1:len(list)])


def main():
    array = [1,2,3,4,5,6]
    print(sum(array))

main()