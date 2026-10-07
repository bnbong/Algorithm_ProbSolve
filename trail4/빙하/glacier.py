from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 모든 0을 체크한 후, 어떤 0이 사방이 1로 둘러싸여있다면 녹일 수 없는 물이므로 pass
# 틱 별로 처리해야하므로 리스트에 후보군들 담아서 bulk로 업데이트하는 방향
# 가생이부터 시작
# 0,0 에서만 bfs

DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def bfs(row, col):
    queue = deque([(row, col)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    melt_target = []

    while queue:
        curr_row, curr_col = queue.popleft()

        for dr, dc in DIRS:
            next_row, next_col = curr_row + dr, curr_col + dc
            if 0 <= next_row < n and 0 <= next_col < m and not visited[next_row][next_col]:
                if a[next_row][next_col] == 0:
                    queue.append((next_row, next_col))
                    visited[next_row][next_col] = True
                else:
                    melt_target.append((next_row, next_col))
                    visited[next_row][next_col] = True

    return melt_target


count = 0
last_bingha = 0

while len(bfs(0, 0)) != 0:
    melt_target = bfs(0, 0)
    last_bingha = len(melt_target)

    for item in melt_target:
        a[item[0]][item[1]] = 0
    count += 1

print(count, last_bingha)