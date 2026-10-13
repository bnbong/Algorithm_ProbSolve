import heapq

n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
INF = int(1e9)
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y, z = edges[i]
    graph[x].append((y, z))
    graph[y].append((x, z))

distance = [INF] * (n+1)

distance[k] = 0

pq = []

heapq.heappush(pq, (0, k))

while pq:
    min_distance, node = heapq.heappop(pq)

    if min_distance != distance[node]:
        continue
    
    for target_idx, target_dist in graph[node]:
        new_dist = distance[node] + target_dist
        if distance[target_idx] > new_dist:
            distance[target_idx] = new_dist
            heapq.heappush(pq, (new_dist, target_idx))

for i in distance[1:]:
    if i != INF:
        print(i)
    else:
        print(-1)