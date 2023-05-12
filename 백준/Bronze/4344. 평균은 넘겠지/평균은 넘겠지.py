C = int(input())

for _ in range(C):
    cases = list(map(int, input().split()))
    student_number = cases[0]
    sum_of_grades = sum(cases[1:student_number+1])

    average = sum_of_grades/student_number

    selected_student = 0

    for student in cases[1:]:
        if average < student:
            selected_student += 1
    
    result = round((selected_student/student_number)*100, 3)
    print('%.3f' % result + "%")
