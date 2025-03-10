import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for r in graph:
    for c in r:
        print(c, end=" ")
    print()
