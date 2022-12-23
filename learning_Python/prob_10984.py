def prob_10984():
    T = int(input())

    for _ in range(T):
        N = int(input())
        credit = 0
        grade = 0
        for _ in range(N):
            C, G = map(float, input().split())
            credit += int(C)
            grade += G * C
        grade = round(grade / credit, 1)
        print(credit, grade)

prob_10984()
