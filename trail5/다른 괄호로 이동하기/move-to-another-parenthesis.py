import heapq

n, a, b = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# Please write your code here.
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
INF = int(1e9)


def dijkstra(start_i, start_j):
    dist = [[INF for _ in range(n)] for _ in range(n)]
    pq = []
    dist[start_i][start_j] = 0
    heapq.heappush(pq, (0, start_i, start_j))

    while pq:
        min_dist, min_i, min_j = heapq.heappop(pq)

        if min_dist != dist[min_i][min_j]:
            continue
        
        for dr, dc in DIRS:
            nr, nc = min_i + dr, min_j + dc
            if 0 <= nr < n and 0 <= nc < n:
                if grid[min_i][min_j] != grid[nr][nc]:
                    target_dist = b
                else:
                    target_dist = a
                
                next_dist = target_dist + dist[min_i][min_j]

                if next_dist < dist[nr][nc]:
                    dist[nr][nc] = next_dist
                    heapq.heappush(pq, (next_dist, nr, nc))
    
    result = dist[0][0]
    for i in range(n):
        for j in range(n):
            if dist[i][j] > result:
                result = dist[i][j]
    
    return result



graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        graph[i][j] = dijkstra(i, j)


result = graph[i][j]

for i in range(n):
    for j in range(n):
        if graph[i][j] > result:
            result = graph[i][j]

print(result)
