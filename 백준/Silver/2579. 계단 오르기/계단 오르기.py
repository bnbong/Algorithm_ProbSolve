import sys

stairs = int(sys.stdin.readline())
points = []

for _ in range(stairs):
    point = int(sys.stdin.readline())
    points.append(point)

dp = [0] * 300
dp[0] = points[0]

if stairs > 1:
    dp[1] = points[0] + points[1]
if stairs > 2:
    dp[2] = max(points[0] + points[2], points[1] + points[2])
if stairs > 3:
    for i in range(3, stairs):
        dp[i] = max(dp[i-3] + points[i-1] + points[i], dp[i-2] + points[i])

print(dp[stairs-1])
