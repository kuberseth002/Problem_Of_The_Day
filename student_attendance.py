day1 = ["Ankit", "Abhi", "Candy"]
day2= ["Abhi", "Ankit"]
day3= ["Candy", "Ankit", "Abhi"]



days = [day1,day2,day3]


attendance = {}



for day in days:
    for student in day:
        if student in attendance:
            attendance[student] += 1
        else:
            attendance[student] = 1

print(f"Total Attendance:{attendance}")









