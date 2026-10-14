import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.


visited = [False] * (n+1)
reversed_order = []
graph = [[] for _ in range(n+1)]

for e in edges:
    a, b = e
    graph[a].append(b)

def dfs(x):
    global visited, reversed_order

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
    
    reversed_order.append(x)


for i in range(1, n+1):
    if visited[i] == False:
        visited[i] = True
        dfs(i)

print(*reversed(reversed_order))