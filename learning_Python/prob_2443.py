def prob_2443():
    N = int(input())
    for _ in range(1, N+1):
        star_num = 2 * N - (_ * 2 - 1)
        print(' ' * (_ - 1) + '*' * star_num)

prob_2443()
