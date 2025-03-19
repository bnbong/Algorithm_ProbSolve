import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())

graph = []
days = 0

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1  # 기존 날짜 +1
                queue.append((nx, ny))


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()

for row in graph:
    if 0 in row:
        print(-1)
        exit()
    days = max(days, max(row))  # 최대 날짜 찾기

print(days-1)
