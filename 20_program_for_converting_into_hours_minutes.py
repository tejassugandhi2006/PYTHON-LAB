# write a python program tht takes a total number of minutes as input and converts it into hours and remaining minutes $\arrow$ 2 hours and ten minutes
minutes = int(input("Enter total minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(hours, "hours and", remaining_minutes, "minutes")
