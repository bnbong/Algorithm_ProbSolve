from collections import deque

DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))   # 상 하 좌 우

def solution(maps):
    n, m = len(maps), len(maps[0])

    dist = [[0] * m for _ in range(n)]       # 0 = 미방문
    dist[0][0] = 1                           # 시작 칸도 1칸
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()

        if (r, c) == (n - 1, m - 1):         # 도착 → 최단 거리 확정
            return dist[r][c]

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m \
               and maps[nr][nc] == 1 and dist[nr][nc] == 0:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))           # 넣을 때 방문 처리

    return -1                                # 큐가 비었는데 도착 못 함