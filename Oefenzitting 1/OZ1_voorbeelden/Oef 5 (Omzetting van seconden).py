input_seconds = int(input("Time in seconds: "))
day_value_in_seconds = 60 * 60 * 24

amount_days = int(input_seconds / day_value_in_seconds)
input_seconds -= amount_days * day_value_in_seconds
amount_hours = int(input_seconds / day_value_in_seconds * 24)
input_seconds -= amount_hours * day_value_in_seconds * 24
amount_minutes = int(input_seconds / day_value_in_seconds * 24 * 60)
amount_seconds = input_seconds - amount_minutes * 60

print(str(amount_days) + " day(s)," + str(amount_hours) + " hour(s)," + str(amount_minutes) + " minute(s)," + str(amount_seconds) + " second(s),")