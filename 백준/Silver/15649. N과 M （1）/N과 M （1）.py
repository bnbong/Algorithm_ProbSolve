"""
BOJ - 15649 N과 M (1)

종료 조건 -> 진행조건 -> 선택 -> 복구 과정

# 1. permutations()를 호출하여 순열을 구한다.
"""
from itertools import permutations


N, M = map(int, input().split())
arrays = [i for i in range(1, N + 1)]

# 1. permutations()를 호출하여 순열을 구한다.
result = permutations(arrays, M)
first = True

for item in result:
    if not first:
        print()
    print(*item, end="")
    first = False
