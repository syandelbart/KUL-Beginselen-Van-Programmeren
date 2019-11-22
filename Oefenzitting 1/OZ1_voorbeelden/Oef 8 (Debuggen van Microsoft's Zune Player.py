#debugged version (too lazy for adding bugged version again)
from calendar import isleap

ORIGIN_YEAR = 1980
days = int(input("Days since 1st January " + str(ORIGIN_YEAR)))

year = ORIGIN_YEAR
while days > 365:
    if isleap(year):
        days -= 366
    else:
        days -= 365
    year += 1

print("The current year: ", year)