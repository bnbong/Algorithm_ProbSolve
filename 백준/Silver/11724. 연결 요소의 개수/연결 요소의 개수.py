import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (N+1)

for i in range(1, N+1):
    if not visited[i]:
        # visited[i] == False 이면 dfs 수행해서 visited check.
        # 아니면 pass
        dfs(graph, i, visited)
        count += 1

print(count)
