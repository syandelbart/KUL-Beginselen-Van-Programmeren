#bugged version
#grade1 = input("Grade / 20: ")
#grade2 = input("Grade / 20: ")

#grade_sum = grade1 + grade2
#result_scale_100 = grade_sum * (100//2*20)
#result_string = "Grade / 100 = " + str(result_scale_100)
#print(result_string)

#unbugged version
grade1 = float(input("Grade / 20: "))
grade2 = float(input("Grade / 20: "))

grade_sum = grade1 + grade2
result_scale_100 = grade_sum * 5 / 2
result_string = "Grade / 100 = " + str(result_scale_100)
print(result_string)