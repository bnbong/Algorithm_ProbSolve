import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, r, c = map(int, input().split())


def dc(n, r, c):
    if n == 0:
        return 0
    return 2*(r%2)+(c%2) + 4 * dc(n-1, r//2, c//2)

print(dc(n, r, c))