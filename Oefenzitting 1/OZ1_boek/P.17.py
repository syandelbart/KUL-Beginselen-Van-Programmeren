first_time = input("Please enter the first time: ")
second_time = input("Please enter the second time:")

f_hours = int(first_time[0:2])
f_minutes = int(first_time[2:4])
s_hours = int(second_time[0:2])
s_minutes = int(second_time[2:4])

if f_hours > s_hours:
    h_between = f_hours - s_hours
elif s_hours > f_hours:
    h_between = s_hours - f_hours
else:
    h_between = 0

if f_minutes > s_minutes:
    m_between = f_minutes - s_minutes
elif s_minutes > f_minutes:
    m_between = s_minutes - f_minutes
else:
    m_between = 0

print(h_between, "hours", m_between, "minutes")
