def prob_2530():
    hour, minute, sec = map(int, input().split())
    add_sec = int(input())

    result_sec = sec + add_sec
    result_min = minute
    result_hour = hour
    while(result_sec >= 60):
        result_min += 1
        result_sec -= 60

    while(result_min >= 60):
        result_hour += 1
        if (result_hour) >= 24:
            result_hour = 0
        result_min -= 60

    print(result_hour, result_min, result_sec)


prob_2530()