import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs(start):
    visited = [-1] * (N+1)
    
    q = deque()
    q.append(start)
    visited[start] = 0
    
    while q:
        node = q.popleft()
        
        for next in graph[node]:
            if visited[next] == -1:
                visited[next] = visited[node] + 1
                q.append(next)
    
    total = sum(visited)
    return total


min_total = float("INF")
ans = 0
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N+1):
    total = bfs(i)
    
    if total < min_total:
        min_total = total
        ans = i

print(ans)
