blue = 0
white = 0

N = int(input())

paper = [[0]] * N

for i in range(N):
    paper[i] = list(map(int, input().split()))


def devide_conq(x, y, N):
    global blue, white

    _cnt = 0

    for i in range(y, y + N):
        for j in range(x, x+N):
            if paper[i][j]:
                _cnt += 1

    if not _cnt:
        white += 1
    elif _cnt == N**2:  # all blue
        blue +=1
    else:
        devide_conq(x, y, N//2)
        devide_conq(x + N//2, y, N//2)
        devide_conq(x, y + N//2, N//2)
        devide_conq(x + N//2, y + N//2, N//2)
    return


devide_conq(0, 0, N)
print(white)
print(blue)
