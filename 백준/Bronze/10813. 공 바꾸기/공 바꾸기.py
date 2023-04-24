N, M = map(int, input().split())
basket = [0] * (N+1)
for x in range(N+1):
    basket[x] = x

for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[j]
    basket[j] = basket[i]
    basket[i] = temp

for item in basket[1:]:
    print(item, end=' ')
