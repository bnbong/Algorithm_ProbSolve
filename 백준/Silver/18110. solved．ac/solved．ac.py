import sys
from collections import deque
from decimal import Decimal, ROUND_HALF_UP

input = sys.stdin.readline

n = int(input())


def c_round(val, places=0):
    p = '1.' + '0' * places if places > 0 else '1'
    return Decimal(str(val)).quantize(Decimal(p), rounding=ROUND_HALF_UP)


if n == 0:
    print(0)
else:
    diffs = []

    for _ in range(n):
        diffs.append(int(input()))

    diffs.sort()
    if n > 3:
        excludes = int(c_round(n*0.15))
        real = diffs[excludes:-excludes]
        print(int(c_round(sum(real)/len(real))))
    else:
        print(int(c_round(sum(diffs)/len(diffs))))
