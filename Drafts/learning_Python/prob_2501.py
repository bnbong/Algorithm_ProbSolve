def prob_2501():
    n, k = map(int, input().split())

    yaksu = []
    for i in range(1, n + 1):
        if n % i == 0:
            yaksu.append(i)
    try:
        print(yaksu[k-1])
    except IndexError:
        print(0)

prob_2501()
