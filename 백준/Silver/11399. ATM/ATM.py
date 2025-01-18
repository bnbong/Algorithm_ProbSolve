N = int(input())

times = []
result = 0

P = input().split()

for p in P:
    times.append(int(p))

times.sort()

for i in range(len(times)):
    result_p = 0
    for j in range(i):
        result_p += times[j]
    result += result_p

print(result + sum(times))
