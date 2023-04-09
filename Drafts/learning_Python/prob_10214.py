def prob_10214():
    test_cases = int(input())

    for i in range(test_cases):
        Y = K = 0

        for _ in range(9):
            y, k = map(int, input().split())
            Y += y
            K += k

        if Y > K:
            print("Yonsei")
        elif Y < K:
            print("Korea")
        else:
            print("Draw")

prob_10214()