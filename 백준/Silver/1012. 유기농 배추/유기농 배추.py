import sys
sys.setrecursionlimit(10**6)


def bfs(start_row, start_col):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        next_row = start_row + dx[i]
        next_col = start_col + dy[i]

        if 0 <= next_row < M and 0 <= next_col < N and batchu[next_col][next_row] == '1':
            batchu[next_col][next_row] = 'X'
            bfs(next_row, next_col)


T = int(input())


for _ in range(T):
    M, N, K = map(int, input().split())

    bugs = 0
    batchu = [['0' for _ in range(M)] for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        batchu[Y][X] = '1'

    for i in range(M):
        for j in range(N):
            if batchu[j][i] == '1':
                bfs(i, j)
                bugs += 1

    print(bugs)
