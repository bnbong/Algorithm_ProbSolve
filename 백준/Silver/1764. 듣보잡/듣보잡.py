N, M = map(int, input().split())

dut = set()
bo = set()

for n in range(N):
    _ = input()
    dut.add(_)

for m in range(M):
    _ = input()
    bo.add(_)

result = []

for i in dut:
    if i in bo:
        result.append(i)

result.sort()
print(len(result))
for _ in result:
    print(_)
