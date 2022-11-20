def prob_2476():
    N = int(input())

    prizes = []

    for i in range(N):
        a, b, c = map(int, input().split())

        if a == b == c:
            prize = 10000 + a * 1000
        elif a == b != c:
            prize = 1000 + a * 100
        elif b == c != a:
            prize = 1000 + b * 100
        elif c == a != b:
            prize = 1000 + c * 100
        else:
            max_number = max(a, b, c)
            prize = max_number * 100
        prizes.append(prize)
    
    print(max(prizes))

def another_2476():
    from collections import Counter

    N = int(input())
    prizes = []

    for n in range(N):
        dice = list(map(int, input().split()))
        cnt = Counter(dice)

        if 3 in cnt.values():
            prizes.append(10000 + 1000 * dice[0])
        elif 2 in cnt.values():
            for i in cnt.keys():
                if cnt[i] == 2:
                    prizes.append(1000 + 100 * i)
        else:
            prizes.append(max(dice) * 100)

    print(max(prizes))


prob_2476()