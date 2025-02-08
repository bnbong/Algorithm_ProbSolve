import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        node = q.popleft()

        if node == K:
            print(visited[node])
            break

        for movement in (node - 1, node + 1, node * 2):
            if 0 <= movement <= max_len and not visited[movement]:
                visited[movement] = visited[node] + 1
                q.append(movement)


N, K = map(int, input().split())
max_len = 100000
visited = [0] * (max_len + 1)
bfs(N)
