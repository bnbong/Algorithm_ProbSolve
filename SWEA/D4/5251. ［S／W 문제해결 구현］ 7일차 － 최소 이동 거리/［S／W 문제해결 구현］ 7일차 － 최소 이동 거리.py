"""
SWEA - 5251 최소 이동 거리

구간의 시작점과 끝의 연결지점 번호, 길이가 주어졌을 때 최소한의 거리로 0번에서 N번으로 이동하려면??

- 각 노드까지의 최단 거리를 저장할 배열(distance)을 아주 큰 값(INF)으로 초기화함.
   - 시작점(0번 노드)의 누적 거리를 0으로 설정하고 우선순위 큐(heapq)에 삽입.
   - 큐에서 '현재까지의 누적 거리가 가장 짧은 노드'를 꺼내어 인접한 노드들을 탐색.
   - (현재 노드까지의 거리 + 다음 간선 거리)가 기존에 기록된 (다음 노드까지의 최단 거리)보다 짧다면,
     최단 거리를 갱신하고 큐에 새로운 정보 (갱신된 거리, 다음 노드)를 push.

# 1. 테스트 케이스 입력을 받는다. T / N, E / s(구간 시작 지점), e(구간 끝지점), w(구간 거리)
# 2. 그래프의 시작점부터 시작해서,
    # 2-1. 각 노드까지의 최단 거리를 기록하는 테이블 (INF로 초기화)
    # 2-2. 시작 노드 초기화 (우선순위 큐: (누적 거리, 현재 노드))
    # 2-3. 큐에서,
        # 2-3-1. 누적 거리가 가장 짧은 노드를 꺼낸다.
        # 2-3-2. 이미 처리된 적 있는(더 짧은 경로가 존재하는) 노드라면 무시
        # 2-3-3. 현재 노드와 연결된 인접 노드들을 확인한다.
        # 2-3-4. 더 짧은 경로를 발견한 경우 distance 테이블을 갱신하고 큐에 삽입
    # 2-4. N에서 끝나므로 N번 노드에 저장된 최단 거리 반환
# 3. 출력한다.
"""
import heapq

from typing import Dict


N: int
E: int
graph: Dict
INF: int = int(1e9)


def find_shortest_path(start: int) -> int:
    # 2-1. 각 노드까지의 최단 거리를 기록하는 테이블 (INF로 초기화)
    distance = [INF] * (N + 1)

    # 2-2. 시작 노드 초기화 (우선순위 큐: (누적 거리, 현재 노드))
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        # 2-3-1. 누적 거리가 가장 짧은 노드를 꺼낸다.
        current_dist, current_node = heapq.heappop(pq)

        # 2-3-2. 이미 처리된 적 있는(더 짧은 경로가 존재하는) 노드라면 무시
        if current_dist > distance[current_node]:
            continue

        # 2-3-3. 현재 노드와 연결된 인접 노드들을 확인한다.
        for next_node, weight in graph[current_node]:
            cost = current_dist + weight

            # 2-3-4. 더 짧은 경로를 발견한 경우 distance 테이블을 갱신하고 큐에 삽입
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    # 2-4. N에서 끝나므로 N번 노드에 저장된 최단 거리 반환
    return distance[N]


def input_test_case() -> None:
    global N, E, graph
    graph = {}
    N, E = map(int, input().split())

    # 그래프 할당
    for i in range(N + 1):
        graph[i] = []

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))


def prob_5251() -> None:
    T: int = int(input().strip())

    for tc in range(1, T+1):
        # 1. 테스트 케이스 입력을 받는다. T / N, E / s(구간 시작 지점), e(구간 끝지점), w(구간 거리)
        input_test_case()

        # 2. 그래프의 시작점부터 시작해서,
        result = find_shortest_path(0)

        # 3. 출력한다.
        print(f"#{tc} {result}")


if __name__ == "__main__":
    prob_5251()
