import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = []


def dfs(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in numbers:
        if i not in result:
            result.append(i)
            dfs(i)
            result.pop()


dfs(numbers[0])
