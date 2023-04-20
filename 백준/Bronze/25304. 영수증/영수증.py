X = int(input())
N = int(input())

sum_of_materials = 0
for i in range(N):
    a, b = map(int, input().split())
    sum_of_materials += a * b

if X == sum_of_materials:
    print("Yes")
else:
    print("No")
