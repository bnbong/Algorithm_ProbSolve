import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())

dut_names = set()
bo_names = set()

for _ in range(N):
    dut = str(input())
    dut_names.add(dut)

for _ in range(M):
    bo = str(input())
    bo_names.add(bo)

intersection = []
for i in dut_names:
    if i in bo_names:
        intersection.append(i)

intersection.sort()
print(len(intersection))
for item in intersection:
    print(str(item))
