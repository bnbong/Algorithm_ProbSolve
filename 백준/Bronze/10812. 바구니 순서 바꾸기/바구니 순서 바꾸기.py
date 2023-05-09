N, M = map(int, input().split())
baguni = [item for item in range(1, N+1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    temp = baguni[k-1:j]
    baguni[k-1:j] = baguni[i-1:k-1]
    baguni[i-1:k-1] = temp

for item in baguni:
    print(item, end=' ')
    