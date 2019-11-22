import random
amount_rows = int(input("Give amount of rows:"))
amount_columns = int(input("Give amount of columns:"))
random_limit = int(input("Give max limit for random integers: "))

matrix = []
for x in range(0,amount_rows):
    for y in range(0, amount_columns):
        matrix.append(random.randint(1,random_limit + 1))

matrix = [5,8,46,2,99,15,4,23,7,84,5,4,35,96,3,25,6,45,1,3,3,5,8,4,6]

for x in range(0,amount_rows):
    for y in range(0, amount_columns):
        print(matrix[amount_rows * x + y],end=" ")
    print()



print("Saddle numbers:",end=" ")
for x in range(0,amount_rows):
    for y in range(0, amount_columns):
        active_num = matrix[x * amount_rows + y]
        is_saddle_number = True
        for sub_x in range(0, amount_rows):
            if x != sub_x:
                #print(matrix[amount_rows * sub_x + y],">",active_num)
                if matrix[amount_rows * sub_x + y] > active_num:
                    is_saddle_number = False
        if is_saddle_number:
            for sub_y in range(0, amount_columns):
                if y != sub_y:
                    #print(matrix[amount_rows * x + sub_y], "<", active_num)
                    if matrix[amount_rows * x + sub_y] < active_num:
                        is_saddle_number = False

        if is_saddle_number:
            print(active_num, end=" ")
        else:
            is_saddle_number = True
            for sub_x in range(0, amount_rows):
                if x != sub_x:
                    #print(matrix[amount_rows * sub_x + y], ">", active_num)
                    if matrix[amount_rows * sub_x + y] < active_num:
                        is_saddle_number = False
            if is_saddle_number:
                for sub_y in range(0, amount_columns):
                    if y != sub_y:
                        #print(matrix[amount_rows * x + sub_y], "<", active_num)
                        if matrix[amount_rows * x + sub_y] > active_num:
                            is_saddle_number = False
        if is_saddle_number:
            print(active_num,end=" ")
print()