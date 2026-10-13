import heapq

n, m = map(int, input().split())
a, b, c = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y, z = edges[i]
    graph[x].append((y, z))
    graph[y].append((x, z))


INF = int(1e9)


def dijkstra(start_node):
    pq = []
    dist = [INF] * (n+1)
    heapq.heappush(pq, (0, start_node))
    dist[start_node] = 0

    while pq:
        min_dist, min_idx = heapq.heappop(pq)

        if min_dist != dist[min_idx]:
            continue
        
        for target_idx, target_dist in graph[min_idx]:
            next_dist = target_dist + dist[min_idx]
            if next_dist < dist[target_idx]:
                dist[target_idx] = next_dist
                heapq.heappush(pq, (next_dist, target_idx))
    
    return dist


result_a = dijkstra(a)
result_b = dijkstra(b)
result_c = dijkstra(c)

result = []

for i in range(1, n+1):
    result.append(min(result_a[i], result_b[i], result_c[i]))

print(max(result))