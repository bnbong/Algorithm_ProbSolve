# 크누스 최적화 풀이
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    numbers = list(map(int, input().split()))
    lists = [[0] * K for _ in range(K)]

    for i in range(K-1):
        lists[i][i+1] = numbers[i] + numbers[i+1]
        for j in range(i+2, K):
            lists[i][j] = lists[i][j-1] + numbers[j]

    for v in range(2, K):
        for i in range(K-v):
            j = i + v
            lists[i][j] += min(lists[i][k] + lists[k+1][j] for k in range(i, j))

    print(lists[0][K-1])
