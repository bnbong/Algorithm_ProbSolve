from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.

DIRS = ((-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))


def knight(row, col):
    queue = deque([(row, col, 0)])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[row][col] = True

    while queue:
        curr_row, curr_col, dist = queue.popleft()

        for dr, dc in DIRS:
            next_row, next_col = curr_row + dr, curr_col + dc

            if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col]:
                if (next_row, next_col) == (r2-1, c2-1):
                    return dist + 1
                queue.append((next_row, next_col, dist+1))
                visited[next_row][next_col] = True
    
    return -1

if r1 == r2 and c1 == c2:
    print(0)
else:
    print(knight(r1-1, c1-1))
