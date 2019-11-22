
amount_x = 22
amount_y = 7
cur_x = 0
cur_y = 0
string = ""

while(cur_y < amount_y):
    while(cur_x < amount_x):
        if cur_y % 2 == 0:
            if(cur_x % 3 == 0):
                string += "+"
            else:
                string += "-"
        else:
            if cur_x % 3 == 0:
                string += "|"
            else:
                string += " "
        cur_x += 1
    print(string)
    cur_y += 1
    string = ""
    cur_x = 0


