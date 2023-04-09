def prob_2525():
    hour, minute = map(int, input().split())
    add_min = int(input())

    result_min = minute + add_min
    result_hour = hour
    while (result_min >= 60):
        result_hour += 1
        if (result_hour) >= 24:
            result_hour = 0

        result_min -= 60


    print(result_hour, result_min)

prob_2525()
