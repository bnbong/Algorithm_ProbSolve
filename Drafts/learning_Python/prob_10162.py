def prob_10162():
    time = int(input())
    a = 0,
    b = 0,
    c = 0
    if time % 10 != 0:
        print(-1)
    else:
        a = int(time/300)
        time = time%300
        b = int(time/60)
        time = time%60
        c = int(time/10)

        print(a, b, c)

prob_10162()