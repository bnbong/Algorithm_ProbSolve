from collections import deque

computers = int(input())
couples = int(input())

counter = 0


def bfs(start_node, graph, counter):
    queue = deque([start_node])
    visited = set([start_node])

    while queue:
        current_node = queue.popleft()

        for next_node in graph[current_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
                counter += 1
    return counter


graph = [[] for _ in range(computers+1)]

for _ in range(couples):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

print(bfs(1, graph, counter))
