def prob_2444():
    N = int(input())
    for _ in range(1, N):
        print(' ' * (N - _) + '*' * (_ * 2 - 1))

    for _ in range(N):
        print(' ' * _ + '*' * (2 * N - 2 * (_) - 1))

prob_2444()
