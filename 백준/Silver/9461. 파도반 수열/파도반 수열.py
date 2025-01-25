T = int(input())

for _ in range(T):
    N = int(input())
    p = [1] * N
    if N == 1:
        print(1)
    elif N == 2:
        print(1)
    elif N == 3:
        print(1)
    else:
        for i in range(3, N):
            p[i] = p[i-2] + p[i-3]
        print(p[N-1])

