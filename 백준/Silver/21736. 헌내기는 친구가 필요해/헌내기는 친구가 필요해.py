import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

school = []
visited = [[0] * M for _ in range(N)]

start_r = 0
start_c = 0
peoples = 0

for i in range(N):
    school.append(list(input().strip()))
    for j in range(M):
        if school[i][j] == 'I':
            start_r, start_c = i, j


def bfs(start_row, start_col):
    global peoples

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[start_row][start_col] = 1
    if school[start_row][start_col] == 'P':
        peoples += 1

    for i in range(4):
        next_row = start_row + dx[i]
        next_col = start_col + dy[i]

        if 0 <= next_row < N and 0 <= next_col < M and visited[next_row][next_col] == 0:
            if school[next_row][next_col] != 'X':
                bfs(next_row, next_col)


bfs(start_r, start_c)

print(peoples if peoples != 0 else "TT")
