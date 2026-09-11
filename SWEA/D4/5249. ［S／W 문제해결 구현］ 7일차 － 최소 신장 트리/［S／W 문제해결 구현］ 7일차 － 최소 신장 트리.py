"""
SWEA - 5249 최소 신장 트리

그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 트리를 MST.

0번 부터 V 까지의 노드, E개의 간선을 가진 가중치 무방향 그래프가 주어지면
이 그래프로부터 최소 신장 트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 작성하라.

마지막 노드 번호 V, 노드는 총 V+1개
간선의 개수는 E개.
간선의 가중치는 w.
주어진 그래프는 항상 모든 노드가 연결되어 있어 최소 신장 트리가 존재한다.

# 1. 테스트 케이스 입력을 받는다. T / V, E / 간선 양 끝 노드 n1, n2, w
# 2. union-find를 class 형식으로 구현한다.
# 3. 가중치 무방향 그래프와 노드 수 V+1을 파라미터로 받는 함수를 구현한다.
    # 3-1. UnionFind class를 초기화.
    # 3-2. 그래프를 간선 가중치를 중심으로 정렬한다. 오름차순으로 정렬되어 서로소 집합 먹이면 최소신장트리 됨.
    # 3-3. 최소 신장 트리를 담을 객체들을 선언한다 : 간선 가중치 합, 최소 신장 트리 리스트
    # 3-4. 파라미터로 들어온 그래프에 요소들을 뽑아,
        # 3-4-1. 서로소 집합이면
        # 3-4-2. 합집합을 수행한 후
        # 3-4-3. 최소신장트리에 넣는다.
# 4. 함수를 실행하여 최소신장트리 가중치 합을 출력한다.
"""
from typing import List, Tuple


V: int
E: int
graph: List[Tuple]


# 2. union-find를 class 형식으로 구현한다.
class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, u: int):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u


# 3. 가중치 무방향 그래프와 노드 수 V+1을 파라미터로 받는 함수를 구현한다.
def kruskal(edges: List, num_nodes: int) -> Tuple[int, List]:
    # 3-1. UnionFind class를 초기화.
    uf: UnionFind = UnionFind(num_nodes)
    # 3-2. 그래프를 간선 가중치를 중심으로 정렬한다. 오름차순으로 정렬되어 서로소 집합 먹이면 최소신장트리 됨.
    edges.sort(key=lambda x: x[2])  # 간선 가중치로 정렬

    # 3-3. 최소 신장 트리를 담을 객체들을 선언한다 : 간선 가중치 합, 최소 신장 트리 리스트
    mst_weight: int = 0
    mst_edges: List = []

    # 3-4. 파라미터로 들어온 그래프에 요소들을 뽑아,
    for u, v, weight in edges:
        # 3-4-1. 서로소 집합이면
        if uf.find(u) != uf.find(v):
            # 3-4-2. 합집합을 수행한 후
            uf.union(u, v)
            # 3-4-3. 최소신장트리에 넣는다.
            mst_weight += weight
            mst_edges.append((u, v, weight))

    return mst_weight, mst_edges


def input_test_case() -> None:
    global V, E, graph

    graph = []
    V, E = map(int, input().split())

    for _ in range(E):
        graph.append(tuple(map(int, input().split())))  # n1, n2, w


def prob_5249() -> None:
    T: int = int(input().strip())

    for tc in range(1, T+1):
        # 1. 테스트 케이스 입력을 받는다. T / V, E / 간선 양 끝 노드 n1, n2, w
        input_test_case()

        # 4. 함수를 실행하여 최소신장트리 가중치 합을 출력한다.
        result, _ = kruskal(graph, V+1)

        print(f"#{tc} {result}")


if __name__ == "__main__":
    prob_5249()
