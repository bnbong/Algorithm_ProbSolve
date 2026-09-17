"""
SWEA - 5258 해피박스

박스에 담긴 물건의 가격합계가 최대가 되도록 물건을 담는다.
물건의 크기와 가격이 주어질 때 A씨가 담을 수 있는 물건 가격은 최대 얼마인가
상품 크기의 합이 박스 크기를 초과 X, 각 상품은 1개씩 있음.

처음 sort를 하고, 가능한 범위 중 가장 큰 것 부터 담는다? -> 안됨.
담을거냐 안담을거냐로 해서 가능한 것들을 합산해서 max 업데이트하는 방식이면 될 듯

# 1. 테스트 케이스 입력을 받는다.
    # 1-1. 상품의 크기를 저장하는 리스트, 상품의 가격을 저장하는 리스트를 만든다.
# 2. 0-1 knapsack을 사용해서,
    # 2-1. 최대 가격을 저장하는 저장소 하나를 초기화한다.
    # 2-2. 상품 정보들을 순회하면서
        # 2-2-1. 역순으로 합산 N의 상품 크기의 최대 가격을 갱신한다.
# 3. 결과를 출력한다.
"""


n: int  # 박스 크기
m: int
weights: list
values: list
dp: list


def input_test_case() -> None:
    global n, m, weights, values

    n, m = map(int, input().split())
    # 1-1. 상품의 크기를 저장하는 리스트, 상품의 가격을 저장하는 리스트를 만든다.
    weights = []
    values = []

    for _ in range(m):
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)


def knapsack():
    global dp

    stocks_length = len(weights)
    # 2-1. 최대 가격을 저장하는 저장소 하나를 초기화한다.
    dp = [0] * (n + 1)

    # 2-2. 상품 정보들을 순회하면서
    for i in range(stocks_length):
        w = weights[i]
        v = values[i]
        # 2-2-1. 역순으로 합산 N의 상품 크기의 최대 가격을 갱신한다.
        for j in range(n, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)

    return dp[n]


def prob_5258() -> None:
    T: int = int(input().strip())

    for tc in range(1, T+1):
        # 1. 테스트 케이스 입력을 받는다.
        input_test_case()

        # 2. 0-1 knapsack을 사용해서,
        result = knapsack()

        # 3. 결과를 출력한다.
        print(f"#{tc} {result}")


if __name__ == "__main__":
    prob_5258()
