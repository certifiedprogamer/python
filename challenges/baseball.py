import csv


with open('cleveland_teams.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_reader = list(csv_reader)
    print(csv_reader)

    attendance_index = csv_reader[0].index("attendance")
    home_run_index = csv_reader[0].index("HR")
    print(attendance_index)
    total_attendance = 0
    g = True
    for i in csv_reader:
        if g == True:
            g = False
            pass
        else:
            total_attendance += int(i[attendance_index])
    home_run_list = list()
    g = True
    for i in csv_reader:
        if g == True:
            g = False
            pass
        else:
            home_run_list.append(int(i[home_run_index]))
    home_run_average = sum(home_run_list) / len(home_run_list)

    print(total_attendance)
    print(home_run_average)
