def prob_10952():
    while True:
        A, B = map(int, input().split())
        if A == B == 0:
            break
        else:
            print(A + B)

prob_10952()
