import sys
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N, M = map(int, input().split())

result = list(combinations(range(1, N+1), M))

for item in result:
    print(" ".join(map(str, item)))
