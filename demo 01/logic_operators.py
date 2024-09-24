# python has 3 logical operators: and, or, and not.
good_attendance = False
good_grades = True
is_student = False
# if good_attendance and good_grades:
# if good_attendance or good_grades:
if is_student and (good_attendance or good_grades):
    print("You can join NTHS!")
elif not is_student:
    print("why are you here")
else:
    print("Not qualified.")
