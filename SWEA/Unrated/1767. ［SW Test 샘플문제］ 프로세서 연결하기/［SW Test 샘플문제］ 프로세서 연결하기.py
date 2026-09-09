"""
SWEA - 1767 프로세서 연결하기

N x N 칸에 전선 혹은 코어 연결. 격자 가장자리에는 전기가 흘러서
가장자리에 설치된 코어는 전선을 연결할 필요가 없음.
전선은 교차 불가

인풋은 이미 코어가 있는 상태로 주어지고 최대한 많은 코어에 전원을 연결했을 때의 전선 길이 구해야함(최소)

델타좌표 방식을 사용해야할 것 같고..

임의로 전선 배치했을 때 해당 전선 칸에 이미 배치한 전선이 있다면 다시 되돌리고(백트래킹) 그 다음 방향에 전선 배치 시도.
최대한 많은 코어에 배치를 시도하기 때문에 모든 코어가 배치 못하는 경우도 있을 것 같음.

격자를 순회하면서 보고 있는 요소가 1(코어) 일 때 전선 깔기 시도.

백트래킹으로 그 다음 코어 위치에서 전선 깔기 시도.

카운트 변수를 두고 min으로 업데이트.

3. 백트래킹 구조: 코어 인덱스 기반 재귀 탐색
for c_i, c_j in cores: 형태의 단순 반복문으로는 전선 연결 여부 조합을 백트래킹할 수 없습니다.
dfs(core_idx, connected_cores, total_length) 형태의 재귀 함수를 만들어 0번 코어 -> 1번 코어 -> ... -> 마지막 코어 순서로 진행해야 합니다.

각 코어마다 시도해야 하는 선택지는 총 5가지입니다:
- 상 방향으로 전선 놓기
- 하 방향으로 전선 놓기
- 좌 방향으로 전선 놓기
- 우 방향으로 전선 놓기
- 전선을 연결하지 않고 그냥 넘어가기 (중요: 모든 코어를 반드시 연결할 수 없는 경우가 있으므로 이 선택지가 필수입니다)

최댓값/최소값 갱신 기준 (문제의 핵심 조건)
최적화 우선순위:
1. 연결된 코어 수가 많은 것 (최대화)
2. 코어 수가 같다면 전선 길이가 짧은 것 (최소화)

기본 min_length 변수 하나만으로 비교하면 안 되고,
(최대 코어 수, 최소 전선 길이)를 쌍(Tuple)으로 관리하거나 비교.
"""
from typing import List, Tuple

DIRS: Tuple = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 상 우 하 좌
n: int
cores: List[Tuple]
grid: List[List[int]]
max_cores: int
min_length: int


def input_testcase() -> None:
    global n, grid
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))


def store_cores() -> None:
    global cores

    cores = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                if 0 < i < n - 1 and 0 < j < n - 1:
                    cores.append((i, j))


def check_can_connect(r: int, c: int, dr: int, dc: int) -> bool:
    nr, nc = r + dr, c + dc

    while 0 <= nr < n and 0 <= nc < n:
        if grid[nr][nc] != 0:  # 코어(1) 혹은 전선(2) 이라면 막힘힘
            return False
        nr += dr
        nc += dc

    return True


# 전선을 까거나(val=2) 치우는(val=0) 함수
def fill_wire(r: int, c: int, dr: int, dc: int, val: int) -> int:
    length = 0
    nr, nc = r + dr, c + dc
    while 0 <= nr < n and 0 <= nc < n:
        grid[nr][nc] = val
        length += 1
        nr += dr
        nc += dc
    return length


def deploy_lines(core_index: int, connected_cores: int, total_length: int) -> None:
    global max_cores, min_length
    # 1. 기저 조건
    if core_index == len(cores):
        # max_cores, min_length 갱신
        # 1. 연결된 코어 수가 많은 것 (최대화)
        # 2. 코어 수가 같다면 전선 길이가 짧은 것 (최소화)
        if max_cores < connected_cores:
            max_cores = connected_cores
            min_length = total_length
        elif max_cores == connected_cores:
            if min_length > total_length:
                min_length = total_length
        return

    r, c = cores[core_index]

    # 2. 4방향 탐색
    for dr, dc in DIRS:
        if check_can_connect(r, c, dr, dc):
            wire_len = fill_wire(r, c, dr, dc, 2)  # 전선 깔기
            deploy_lines(
                core_index + 1, connected_cores + 1, total_length + wire_len
            )
            fill_wire(r, c, dr, dc, 0)  # 백트래킹 (전선 치우기)

    # 3. 전선을 연결하지 않고 그냥 넘어가기 (필수)
    deploy_lines(core_index + 1, connected_cores, total_length)


def prob_1767() -> None:
    global grid, max_cores, min_length
    T: int = int(input().strip())

    for tc in range(1, T + 1):
        # 1. 테스트 케이스 입력을 받는다.
        input_testcase()

        store_cores()
        max_cores = 0
        min_length = 0

        deploy_lines(0, 0, 0)

        print(f"#{tc} {min_length}")


if __name__ == "__main__":
    prob_1767()
