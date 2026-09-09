"""
SWEA - 2117 홈 방범 서비스

방범 서비스는 격자에서 마름모 모양으로 제공.
마름모가 격자를 벗어나도 서비스 비용은 같음.
서비스 비용 = K * k + (k-1) * (k-1)

최대한 많은 집에 마름모 모양을 겹치게 해야함.
출력은 서비스를 받는 집 수.

마름모를 stride 하면서 계산해야하나? 제한시간이 크게 주어진 것으로 봐선 가능성 있을지도

맨해튼 거리 Distance = abs(r1 - r2) + abs(c1 - c2)
중심 좌표가 (r, c)인 마름모 영역은 중심 좌표로부터의 맨해튼 거리가 K-1 이하인 모든 칸
격자 모든 칸을 돌면서 중심점과의 거리가 K-1 이하인지만 판별하면 될 듯.

이익 = 마름모 안 집 수 * M - 서비스 비용

# 1. 테스트 케이스 입력을 받는다.
# 2. result = 0 초기화
# 3. 집 좌표를 저장한다.
# 4. 서비스 영역 K를 1부터 1씩 총 N+1까지 늘려가면서,
    # 4-1. 마름모 중심 좌표를 (0, 0) 부터 체크한다.
    # 4-2. 마름모 범위(|r - 집r| + |c - 집c| <= K - 1) 내라면 범위 내 집 수 +1
    # 4-3. 이익을 계산해서 0 이상인지 확인, 이상이면 집 개수로 result max 업데이트
# 5. 출력한다.
"""
from typing import List, Tuple


N: int
M: int
city: List[List[int]]
houses: List[Tuple]


def input_testcase() -> None:
    global N, M, city
    N, M = map(int, input().split())
    city = []

    for _ in range(N):
        city.append(list(map(int, input().split())))


def save_houses() -> None:
    global houses

    houses = []

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append((i, j))


def check_houses(k: int) -> int:
    service_houses: int = 0
    # 4-1. 마름모 중심 좌표를 (0, 0) 부터 체크한다.
    for i in range(N):
        for j in range(N):
            _houses: int = 0
            # 4-2. 마름모 범위(|r - 집r| + |c - 집c| <= K - 1) 내라면 범위 내 집 수 +1
            for h_i, h_j in houses:
                if abs(i - h_i) + abs(j - h_j) <= k-1:
                    _houses += 1
            # 4-3. 이익을 계산해서 0 이상인지 확인, 이상이면 집 개수로 result max 업데이트
            # 이익 = 마름모 안 집 수 * M - 서비스 비용
            if _houses * M - (k**2 + (k-1)**2) >= 0:
                service_houses = max(service_houses, _houses)

    return service_houses


def prob_2117() -> None:
    T: int = int(input().strip())

    for tc in range(1, T+1):
        # 1. 테스트 케이스 입력을 받는다.
        input_testcase()

        # 2. result = 0 초기화
        result: int = 0

        # 3. 집 좌표를 저장한다.
        save_houses()

        # 4. 서비스 영역 K를 1부터 1씩 총 N+1까지 늘려가면서,
        for k in range(1, N*2):
            result = max(result, check_houses(k))

        print(f"#{tc} {result}")


if __name__ == "__main__":
    prob_2117()
