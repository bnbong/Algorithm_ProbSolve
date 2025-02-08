import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_row = x + dx[i]
            next_col = y + dy[i]

            if 0 <= next_row < N and 0 <= next_col < M and graph[next_row][next_col] == 1:
                queue.append((next_row, next_col))
                graph[next_row][next_col] = graph[x][y] + 1


N, M = map(int, input().split())
graph = []
for _ in range(N):
    lines = list(map(int, input().strip()))
    graph.append(lines)

bfs()
print(graph[N-1][M-1])
