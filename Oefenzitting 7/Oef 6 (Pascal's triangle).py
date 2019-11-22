def pascal(c,r):
    if c==0 and r==0:
        return 1
    else:
        return pascal(c-1,r-1) + pascal(c+1,r-1)


def main():
    pascal(2,0)

main()