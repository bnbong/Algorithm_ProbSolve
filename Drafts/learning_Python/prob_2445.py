def prob_2445():
    N = int(input())

    for _ in range(1, N + 1):
        print('*' * _ + ' ' * (2 * N - 2 * _) + '*' * _)
    
    for _ in range(1, N):
        print('*' * (N - _) + ' ' * 2 * _ + '*' * (N - _))

prob_2445()
