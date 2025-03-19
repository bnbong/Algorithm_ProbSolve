import sys
from itertools import permutations


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

result = sorted(list(permutations(numbers, M)))

result = sorted(list(set(result)))

for item in result:
    for i in item:
        print(i, end=' ')
    print("")
