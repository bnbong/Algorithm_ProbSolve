"""
SWEA - 5263 그래프 최소 비용

특정 노드로 최소 비용으로 간다고 했을 때 가장 큰 비용을 출력

모든 노드를 갈 수 있는 길이 있다.
모든 노드에 대해서 구해야하므로 플로이드 워셜을 써야함

모든 노드 쌍(All-Pairs) 간의 최단 거리를 구한 뒤, 그중 최댓값을 찾는 문제.
노드 개수 N이 작고 모든 출발점-도착점 간 최단 경로를 구해야 하므로, 플로이드-워셜

# 1. 테스트 케이스 입력을 받는다. T / N / a_ij
# 2. 인접 행렬에 예외처리를 하고 초기화를 한다.
    # 2-1. 자기 자신이 아닌데 0이면 이동이 불가한 곳이므로 INF로 변경하여 갱신 제외
# 3. 경유지, 출발지, 목적지 순서로 3중 for문을 돌아 인접 행렬을 업데이트,
    # 3-1. matrix[i][k] 또는 matrix[k][j]가 INF이면 제외
    # 3-2. matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
# 4. 가장 최대 요소를 출력하는데 요소가 INF인 것을 제외
"""
from typing import List


N: int
matrix: List[List[int]]
INF: int = int(1e9)


def update_min_distance_table() -> None:
    global matrix

    # 3. 경유지, 출발지, 목적지 순서로 3중 for문을 돌아 인접 행렬을 업데이트,
    for k in range(N):
        for i in range(N):  # 시작 정점
            for j in range(N):  # 도착 정점
                # 3-1. matrix[i][k] 또는 matrix[k][j]가 INF이면 제외
                if matrix[i][k] != INF and matrix[k][j] != INF and matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    # 3-2. matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                    matrix[i][j] = matrix[i][k] + matrix[k][j]


def input_test_case() -> None:
    global N, matrix

    matrix = []
    N = int(input().strip())

    for i in range(N):
        matrix.append(list(map(int, input().split())))

    # 2. 인접 행렬에 예외처리를 하고 초기화를 한다.
    for i in range(N):
        for j in range(N):
            # 2-1. 자기 자신이 아닌데 0이면 이동이 불가한 곳이므로 INF로 변경하여 갱신 제외
            if i != j and matrix[i][j] == 0:
                matrix[i][j] = INF


def prob_5263() -> None:
    T: int = int(input().strip())

    for tc in range(1, T+1):
        # 1. 테스트 케이스 입력을 받는다. T / N / a_ij
        input_test_case()

        update_min_distance_table()

        # 4. 가장 최대 요소를 출력하는데 요소가 INF인 것을 제외
        result = 0
        for i in range(N):
            for j in range(N):
                if matrix[i][j] != INF:
                    result = max(result, matrix[i][j])

        print(f"#{tc} {result}")


if __name__ == "__main__":
    prob_5263()
