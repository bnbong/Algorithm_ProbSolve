from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=' ')
            if start not in graph:
                return visited
            visited.add(node)
            queue.extend(graph[node])

    return visited


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    print(start, end=' ')

    if start not in graph:
        return visited
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


graph = dict()

N, M, V = map(int, input().split())

for _ in range(M):
    a, b = map(int, input().split())

    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

sorted_graph = dict(sorted(graph.items()))
for key in sorted_graph:
    sorted_graph[key].sort()


visited_dfs = dfs(graph, V)
print()
visited_bfs = bfs(graph, V)

