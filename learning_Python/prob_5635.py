def prob_5635():
    from operator import itemgetter

    student_number = int(input())
    students = []

    for _ in range(student_number):
        name, day, month, year = map(str, input().split())
        students.append([name, int(day), int(month), int(year)])
    
    students = sorted(students, key=itemgetter(3, 2, 1))
    print(students[-1][0], students[0][0], sep='\n')

prob_5635()