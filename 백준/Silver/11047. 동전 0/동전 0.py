N, K = map(int, input().split())

coins = []
result = 0

for _ in range(N):
    coins.append(int(input()))

coins.reverse()

for coin in coins:
    if coin > K:
        continue
    result += K // coin
    K %= coin
    if K <= 0:
        break

print(result)
