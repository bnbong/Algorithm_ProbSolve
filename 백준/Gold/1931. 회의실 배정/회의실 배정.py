import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

meetings = []
counts = 0
finished_time = 0

for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: (x[1], x[0]))

for start, end in meetings:
    if finished_time <= start:
        counts += 1
        finished_time = end

print(counts)
