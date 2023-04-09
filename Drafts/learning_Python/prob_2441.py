def prob_2441():
    n = int(input())

    for i in range(n):
        star = '*' * (n - i)
        blank = ' ' * i
        print(blank + star)

prob_2441()