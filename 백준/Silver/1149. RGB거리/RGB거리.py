import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

cost = []

dp = [[0]*3 for _ in range(N)]

for i in range(N):
    cost.append(list(map(int, input().split())))

dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

for j in range(1, N):
    dp[j][0] = min(dp[j - 1][1] + cost[j][0], dp[j - 1][2] + cost[j][0])
    dp[j][1] = min(dp[j - 1][0] + cost[j][1], dp[j - 1][2] + cost[j][1])
    dp[j][2] = min(dp[j - 1][0] + cost[j][2], dp[j - 1][1] + cost[j][2])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
