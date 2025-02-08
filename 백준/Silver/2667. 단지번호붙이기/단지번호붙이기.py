import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs(a, b):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_row = x + dx[i]
            next_col = y + dy[i]

            if 0 <= next_row < N and 0 <= next_col < N and graph[next_row][next_col] == 1:
                graph[next_row][next_col] = 0
                queue.append((next_row, next_col))
                count += 1

    return count


N = int(input())
graph = []

for _ in range(N):
    lines = list(map(int, input().strip()))
    graph.append(lines)

results = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result = bfs(i, j)
            results.append(result)

results.sort()
print(len(results))
for item in results:
    print(item)
