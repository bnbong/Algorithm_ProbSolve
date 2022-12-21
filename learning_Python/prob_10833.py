def prob_10833():
    N = int(input())
    apples = 0
    for _ in range(N):
        A, B = map(int, input().split())
        apples += B % A
    print(apples)

prob_10833()
