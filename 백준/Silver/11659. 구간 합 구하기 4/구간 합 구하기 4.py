import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

_sum = 0
sum_arr = [0]

for i in range(N):
    _sum += arr[i]
    sum_arr.append(_sum)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_arr[j] - sum_arr[i-1])
