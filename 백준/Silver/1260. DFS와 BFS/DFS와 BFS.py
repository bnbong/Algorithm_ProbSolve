import sys
import copy
from collections import defaultdict, deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graphs = defaultdict(list)


def dfs(start, graph, visited=[False]*(N+1)):
    visited[start] = True
    print(start, end=" ")
    for v in graph[start]:
        if not visited[v]:
            dfs(v, graph, visited)


def bfs(start, graph, visited=[False]*(N+1)):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

for i in graphs:
    graphs[i].sort()

graph_d = copy.deepcopy(graphs)
graph_b = copy.deepcopy(graphs)

dfs(V, graph_d)
print()
bfs(V, graph_b)
