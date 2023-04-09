def prob_10103():
    round_amount = int(input())
    A = 100
    B = 100
    for i in range(round_amount):
        a, b = map(int, input().split())
        if a < b:
            A -= b
        elif a > b:
            B -= a
    print(A, B, sep='\n')

prob_10103()