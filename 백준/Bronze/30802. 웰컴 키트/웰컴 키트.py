N = int(input())

S, M, L, XL, XXL, XXXL = map(int, input().split())

T, P = map(int, input().split())

sizes = [S, M, L, XL, XXL, XXXL]

shirt = 0

for i in sizes:
    if i % T == 0:
        shirt += (i // T)
    else:
        shirt += (i // T) + 1

print(shirt)
print(N // P, N % P)
