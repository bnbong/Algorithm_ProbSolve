import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))


visited = [[-1] * m for _ in range(n)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if maps[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if maps[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()
