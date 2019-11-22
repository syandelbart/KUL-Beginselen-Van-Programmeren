import math

side_size = float(input("Give the size of a side of the rectangle: "))

print("Perimeter:", 4 * side_size)
print("Area:", side_size * side_size)
print("Diagonal length:", math.sqrt(side_size ** 2 + side_size ** 2))