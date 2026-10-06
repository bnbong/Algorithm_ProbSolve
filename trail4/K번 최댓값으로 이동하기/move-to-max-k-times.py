from collections import deque


n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())

# Please write your code here.

DIRS = ((-1, 0), (0, -1), (1, 0), (0, 1))


visited = [[False for _ in range(n)] for _ in range(n)]
final_row, final_col = r-1, c-1
moved_count = 0

def move_next(row, col):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[row][col] = True
    queue = deque([(row, col)])
    start_val = grid[row][col]
    candidates = []

    while queue:
        curr_row, curr_col = queue.popleft()

        for dr, dc in DIRS:
            next_row, next_col = curr_row + dr, curr_col + dc

            if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col]:
                if grid[next_row][next_col] < start_val:
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))
                    candidates.append((grid[next_row][next_col], next_row, next_col))
    
    if not candidates:
        return
    
    candidates.sort(key=lambda x: (-x[0], x[1], x[2]))

    return candidates[0][1], candidates[0][2]
                    


for _ in range(k):
    next_pos = move_next(final_row, final_col)
    if next_pos == None:
        break
    final_row, final_col = next_pos


print(final_row+1, final_col+1)