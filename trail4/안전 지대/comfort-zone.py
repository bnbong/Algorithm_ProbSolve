from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_places = 0
max_k = 1

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(row, col, map, visited):
    global max_places

    queue = deque([(row, col)])
    visited[row][col] = True

    while queue:
        curr_row, curr_col = queue.popleft()

        for dr, dc in DIRS:
            next_row, next_col = curr_row + dr, curr_col + dc

            if 0 <= next_row < n and 0 <= next_col < m and not visited[next_row][next_col] and map[next_row][next_col] != FLOODED:
                queue.append((next_row, next_col))
                visited[next_row][next_col] = True


def flood(k):
    new_map = grid[:]
    for i in range(n):
        for j in range(m):
            if grid[i][j] <= k:
                new_map[i][j] = FLOODED
            else:
                new_map[i][j] = grid[i][j]
    
    return new_map


FLOODED = -1
max_height = 0

for i in range(n):
    for j in range(m):
        max_height = max(max_height, grid[i][j])

for k in range(1, max_height+1):
    map = flood(k)
    count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and map[i][j] != FLOODED:
                bfs(i, j, map, visited)
                count += 1
    
    if count > max_places:
        max_places = count
        max_k = k

print(max_k, max_places)
