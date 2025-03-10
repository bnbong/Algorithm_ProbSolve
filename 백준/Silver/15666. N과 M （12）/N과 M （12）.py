import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers = list(set(numbers))
numbers.sort()
ans = []


def back_track(start):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(start, len(numbers)):
        ans.append(numbers[i])
        back_track(i)
        ans.pop()

back_track(0)
