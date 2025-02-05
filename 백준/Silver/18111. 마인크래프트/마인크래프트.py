import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N, M, B = map(int, input().split())

time = [0 for _ in range(257)]  # 땅 높이 별 걸리는 시간
graph = []
result = 0

for _ in range(N):
    graph.extend(map(int, input().split()))

for ground in range(257):
    cur_block = B

    for target_ground in graph:
        if target_ground <= ground:  # 내가 가지고 있는 블록으로 채우는 경우, ground > i
            time[ground] += (ground - target_ground)
            cur_block -= (ground - target_ground)
        else:  # 땅에서 블록 제거 하는 경우, ground < i
            time[ground] += 2 * (target_ground - ground)
            cur_block += (target_ground - ground)

    if cur_block >= 0 and time[ground] <= time[result]:  # 땅이 가장 높은 경우로 fix
        result = ground

print(time[result], result)
