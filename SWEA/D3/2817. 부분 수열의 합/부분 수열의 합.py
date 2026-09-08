"""
SWEA - 2817 부분 수열의 합

수열이 주어졌을 때 최소 1개 이상의 수를 선택해서 그 합이 K가 되는 경우의 수를 구하는 프로그램
같은 값을 골라도 다른 위치의 수를 골랐으면 다른 경우로 봄
수가 만들어지는 경우의 수를 최종 출력

가방에 넣냐 안넣냐로도 풀 수 있을지도?
숫자 요소들 나열된 것에서 숫자들 돌면서 어떤 숫자 포함할지 안할지를 0/1로 함.

# 1. 테스트 케이스 입력을 받는다. T / N, K / 수열
# 2. 돌고 있는 인덱스의 수열을 바탕으로 합을 구해 나가는데,
    # 2-1. 목표값 K를 달성한 경우 경우의 수 증가 후 종료
    # 2-2. start_idx부터 원소를 하나씩 선택
    # 2-3. K를 초과하면 그 뒤의 더 큰 원소들도 볼 필요 없이 바로 break
    # 2-4. 다음 원소를 선택하고 재귀 호출
# 3. 출력한다.
"""
from typing import List


N: int
K: int
numbers: List[int]
count: int


def input_test_cases() -> None:
    """테스트 케이스 인풋을 받는 함수.

    :return: None
    """
    global N, K, numbers

    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 효율적으로 K라는 수를 만드는 경우를 찾기 위해 정렬.
    numbers.sort()


def backtrack(start_idx: int, current_sum: int) -> None:
    global count
    # 2-1. 목표값 K를 달성한 경우 경우의 수 증가 후 종료
    if current_sum == K:
        count += 1
        return

    # 2-2. start_idx부터 원소를 하나씩 선택
    for i in range(start_idx, N):
        # 2-3. K를 초과하면 그 뒤의 더 큰 원소들도 볼 필요 없이 바로 break
        if current_sum + numbers[i] > K:
            break

        # 2-4. 다음 원소를 선택하고 재귀 호출
        backtrack(i + 1, current_sum + numbers[i])


def prob_2817() -> None:
    """메인 호출 함수

    :return: None
    """
    global count

    T: int = int(input().strip())

    for tc in range(1, T+1):
        # 1. 테스트 케이스 입력을 받는다. T / N, K / 수열
        input_test_cases()

        # 2. 돌고 있는 인덱스의 수열을 바탕으로 합을 구해 나가는데,
        count = 0
        backtrack(0, 0)

        # 3. 출력한다.
        print(f"#{tc} {count}")


if __name__ == "__main__":
    prob_2817()
