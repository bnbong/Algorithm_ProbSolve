def prob_10156():
    k, n, m = map(int, input().split())

    result = 0
    if not k * n < m:
        result = k * n - m
    print(result)

prob_10156()