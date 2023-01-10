def prob_9295():
    T = int(input())
    for _ in range(1, T + 1):
        a, b = map(int, input().split())
        print('Case %s: %d' % (_, a + b))

prob_9295()
