def prob_12865():
    N, K = map(int, input().split())
    stuffs = [[0, 0]]
    knapsack = [[0] * (K+1) for _ in range(N+1)]
    for _ in range(1, N + 1):
        stuffs.append(list(map(int, input().split())))

    for i in range(1, N + 1):
        for k in range(1, K + 1):
            w, v = stuffs[i]
            if k >= w:
                knapsack[i][k] = max(v + knapsack[i-1][k-w], knapsack[i-1][k])
            else:
                knapsack[i][k] = knapsack[i-1][k]
    print(knapsack[i][k])

prob_12865()