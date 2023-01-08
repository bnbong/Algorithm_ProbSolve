def prob_10797():
    days_first = int(input())
    cars = list(map(int, input().split()))
    result = 0

    for car in cars:
        if days_first == car:
            result += 1

    print(result)

prob_10797()
