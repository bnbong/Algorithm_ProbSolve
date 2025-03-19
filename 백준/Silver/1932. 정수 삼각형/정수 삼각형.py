import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

tri = []

for _ in range(N):
    tri.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i+1):
        if j == 0:  # 오른쪽 대각선만 선택 가능
            tri[i][j] += tri[i-1][j]
        elif j == i:  # 왼쪽 대각선만 선택 가능
            tri[i][j] += tri[i-1][j-1]
        else:  # 양 쪽 대각선 둘 다 선택 가능
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[N-1]))
