def prob_5063():
    test_cases = int(input())

    for i in range(test_cases):
        r, e, c = map(int, input().split())

        if e - r < c:
            print("do not advertise")
        elif e - r == c:
            print("does not matter")
        else:
            print("advertise")

prob_5063()