def prob_2921():
    n = int(input())
    result = 0
    for i in range(0, n + 1):
        for j in range(i, n + 1):
            result += i + j
    print(result)

prob_2921()
