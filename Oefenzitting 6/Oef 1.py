m = int(input("Lower bound (m): "))
n = int(input("Upper bound (n): "))

even_set = set()
three_set = set()


if m % 2 != 0:
    m += 1
for counter in range(m,n+1,2):
    even_set.add(counter)


if m % 3 != 0:
    m += 3 - (m % 3)
for counter in range(m,n+1,3):
    three_set.add(counter)

#Divisible by 6
print(three_set.intersection(even_set))

#Odd numbers divisible by 3
print(three_set.difference(even_set))

#Divisible by either 2 / 3
print(even_set.union(three_set))