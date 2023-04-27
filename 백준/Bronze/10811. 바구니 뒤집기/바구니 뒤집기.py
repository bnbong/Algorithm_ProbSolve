N, M = map(int, input().split())
baguni = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = baguni[i-1:j]
    temp.reverse()
    baguni[i-1:j] = temp

for item in baguni:
    print(item, end =' ')
