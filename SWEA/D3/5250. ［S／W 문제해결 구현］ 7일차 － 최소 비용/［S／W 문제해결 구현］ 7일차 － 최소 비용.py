"""
SWEA - 5250 최소비용

N * N 격자의 각 칸에 높이 H가 적혀 있음
출발 = (0, 0), 도착 = (N-1, N-1), 상하좌우로만 이동 (대각선 불가)

이동 비용
    기본 1
    더 높은 곳으로 갈 때만 높이 차이만큼 추가
    -> cost = 1 + max(0, 다음 높이 - 현재 높이)
    내려가거나 같은 높이면 추가 비용 없음 (음수로 깎이면 안됨)

출발지에서 도착지까지의 최소 연료 소비량을 출력

가중치가 있으니 BFS가 아니라 다익스트라 써야할듯
간선 비용에 음수 X.

방향 이동이 있으니 dx, dy 방식 써야할듯

-> 두 칸 사이의 이동 비용을 계산하는 함수
-> 격자 범위 안인지 확인하는 함수
-> 다익스트라로 최소 연료를 구하는 함수

# 1. 테스트 케이스 입력을 받는다. T / N / N * N 크기의 정사각 배열
# 2. 최소 연료 소비량을 다익스트라로 구한다.
    # 2-1. 비용 테이블을 INF로 초기화하고 출발 칸만 0으로 둔다.
    # 2-2. 우선순위 큐에 (누적 비용, 행, 열)을 넣는다.
    # 2-3. 큐에서 누적 비용이 가장 작은 칸을 꺼낸다.
        # 2-3-1. 이미 더 싼 경로로 처리된 칸이면 무시
        # 2-3-2. 도착 칸이면 그 비용이 최소값이므로 즉시 반환
    # 2-4. 상하좌우 인접 칸을 확인한다.
        # 2-4-1. 격자 범위를 벗어나면 건너뛴다.
        # 2-4-2. 이동 비용을 계산한다. (기본 1 + 올라간 높이차)
        # 2-4-3. 더 싼 경로면 비용 테이블을 갱신하고 큐에 넣는다.
# 3. 출력한다.
"""
import heapq
from typing import List, Tuple


INF: int = int(1e9)
DIRS: Tuple[Tuple[int, int], ...] = ((-1, 0), (1, 0), (0, -1), (0, 1))
T: int
n: int


def calc_fuel(current_height: int, next_height: int) -> int:
    # 2-4-2. 이동 비용을 계산한다. (기본 1 + 올라간 높이차)
    diff: int = next_height - current_height

    return 1 + diff if diff > 0 else 1


def min_fuel(board: List[List[int]], n: int) -> int:
    # 2-1. 비용 테이블을 INF로 초기화하고 출발 칸만 0으로 둔다.
    costs: List[List[int]] = [[INF] * n for _ in range(n)]
    costs[0][0] = 0

    # 2-2. 우선순위 큐에 (누적 비용, 행, 열)을 넣는다.
    priority_queue: List[Tuple[int, int, int]] = [(0, 0, 0)]

    while priority_queue:
        # 2-3. 큐에서 누적 비용이 가장 작은 칸을 꺼낸다.
        current_cost, row, col = heapq.heappop(priority_queue)

        # 2-3-1. 이미 더 싼 경로로 처리된 칸이면 무시
        if current_cost > costs[row][col]:
            continue

        # 2-3-2. 도착 칸이면 그 비용이 최소값이므로 즉시 반환
        if row == n - 1 and col == n - 1:
            return current_cost

        # 2-4. 상하좌우 인접 칸을 확인한다.
        for d_row, d_col in DIRS:
            next_row, next_col = row + d_row, col + d_col

            # 2-4-1. 격자 범위를 벗어나면 건너뛴다.
            if not (0 <= next_row < n and 0 <= next_col < n):
                continue

            fuel: int = calc_fuel(board[row][col], board[next_row][next_col])
            next_cost: int = current_cost + fuel

            # 2-4-3. 더 싼 경로면 비용 테이블을 갱신하고 큐에 넣는다.
            if next_cost < costs[next_row][next_col]:
                costs[next_row][next_col] = next_cost
                heapq.heappush(priority_queue, (next_cost, next_row, next_col))

    return costs[n - 1][n - 1]


def solve() -> None:
    global T, n
    # 1. 테스트 케이스 입력을 받는다. T / N / N * N 크기의 정사각 배열
    T = int(input().strip())

    for tc in range(1, T + 1):
        n = int(input().strip())
        board: List[List[int]] = [
            list(map(int, input().split())) for _ in range(n)
        ]

        # 2. 최소 연료 소비량을 다익스트라로 구한다.
        answer: int = min_fuel(board, n)

        # 3. 출력한다.
        print(f"#{tc} {answer}")


if __name__ == "__main__":
    solve()
