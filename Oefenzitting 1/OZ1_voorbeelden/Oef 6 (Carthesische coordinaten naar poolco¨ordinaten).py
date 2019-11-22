import math

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

radius = math.sqrt(x ** 2 + y ** 2)
theta = math.atan(x/y)

print("The radius is: " + str(radius))
print("Theta is: " + str(theta))