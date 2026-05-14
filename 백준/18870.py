import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
x_list = list(map(int, input().split()))

sorted_x_list = sorted(list(set(x_list)))

comp = dict(zip(sorted_x_list, list(range(len(sorted_x_list)))))
for item in x_list:
    print(comp[item], end=' ')
