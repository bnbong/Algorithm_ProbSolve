import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

_heap = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(_heap)[1])
        except IndexError:
            print(0)
    else:
        heapq.heappush(_heap, (abs(x), x))
