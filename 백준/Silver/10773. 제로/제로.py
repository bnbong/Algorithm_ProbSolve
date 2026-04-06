import sys

input = sys.stdin.readline

K = int(input())

moneys = []

for _ in range(K):
    number = int(input())
    if number != 0:
        moneys.append(number)
    else:
        target = moneys[-1]
        moneys.reverse()
        moneys.remove(target)
        moneys.reverse()

print(sum(moneys))
