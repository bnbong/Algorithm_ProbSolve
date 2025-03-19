import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (N+1)


def dfs(s):
    for i in tree[s]:
        if visited[i] == 0:
            visited[i] = s  # visited에 방문한 부모 노드 입력
            dfs(i)


dfs(1)


for j in range(2, N+1):
    print(visited[j])
