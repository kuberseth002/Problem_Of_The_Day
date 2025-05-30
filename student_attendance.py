def track_attendance(day1, day2, day3, day4):
    """
    Tracks the number of days each student was present.

    Parameters:
    day1, day2, day3, day4: Lists containing student names present on each day.

    Returns:
    A dictionary with student names as keys and attendance count as values.
    """
    attendance = {}
    
    all_days = [day1, day2, day3, day4]

    for day in all_days:
        for student in day:
            student = student.strip().title() 
            if student in attendance:
                attendance[student] += 1
            else:
                attendance[student] = 1
    return attendance

day1 = ["karan", "bobby", "candy"]
day2 = ["Bobby", "candy", "dolly"]
day3 = ["karan", "dolly", "evana"]
day4 = ["karan", "bobby", "evana"]

result = track_attendance(day1, day2, day3, day4)

print("Student Attendance Summary:")
for student in sorted(result):
    print(student + ":", result[student], "days")
