def prob_1546():
    n = int(input())
    grades = list(map(int, input().split()))
    new_grades = []

    for grade in grades:
        new_grade = grade / max(grades) * 100
        new_grades.append(new_grade)

    result = 0
    for grade in new_grades:
        result += grade
    result = result / len(new_grades)

    print(result)

prob_1546()
