def maximum(list,max = 0):
    if(len(list) == 0):
        return max
    else:
        print(list)
        if(list[0] > max):
            max = list[0]
        return maximum(list[1:len(list)],max)


def main():
    array = [2,3,6,4,4,1,5,6,6,0,12]
    print(maximum(array))

main()