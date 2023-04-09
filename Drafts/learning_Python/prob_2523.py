def prob_2523():
    N = int(input())
    for _ in range(1, N + 1):
        print('*' * _)
    for _ in range(1, N):
        print('*' * (N - _))

prob_2523()
