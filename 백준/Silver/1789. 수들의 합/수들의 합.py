import sys

input = sys.stdin.readline

S = int(input())

i = 1
sums = 0

while True:
    sums += i
    if sums > S:
        i = i-1
        break
    elif sums == S:
        break
    i += 1

print(i)