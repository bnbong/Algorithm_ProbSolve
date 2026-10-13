import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y, z = edges[i]
    graph[y].append((x, z))

INF = int(1e9)

dist = [INF] * (n+1)
pq = []

dist[n] = 0

heapq.heappush(pq, (0, n))

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if min_dist != dist[min_idx]:
        continue
    
    for target_idx, target_dist  in graph[min_idx]:
        next_dist = target_dist + dist[min_idx]
        if next_dist < dist[target_idx]:
            dist[target_idx] = next_dist
            heapq.heappush(pq, (next_dist, target_idx))

result = dist[1]

for i in dist:
    if i != INF and result < i:
        result = i

print(result)