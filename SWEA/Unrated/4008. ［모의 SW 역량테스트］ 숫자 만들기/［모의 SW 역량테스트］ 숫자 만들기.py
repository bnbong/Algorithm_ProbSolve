"""
SWEA - 4008 숫자 만들기

숫자들 사이에 연산자 넣어서 최소 / 최대 뽑아 두 수 차이 구하는 문제.
연산자 카드 개수가 주어지고 그 개수를 적절히 배치해야함.

연산자 우선순위는 고려 안해서 다행...
permutations를 쓰면 계산 전에 경우의 수를 너무 많이 생성할 것 같음.
연산자 카드의 남은 개수를 매개변수로 넘겨주면서 숫자를 하나씩 계산해나가는 방식이 좋을 것 같음.

백트래킹
- 현재 탐색 중인 숫자의 위치 인덱스
- 현재 계산된 누적 결과값
- 남은 연산자 개수
    종료 시점
    - 숫자 인덱스가 마지막 끝에 도달하면 모두 끝
    - 누적 결과값을 max 값 및 min 값 업데이트 후 return

적용
- 현재 남은 연산자 카드 중 1개 이상 남아있는 연산자 선택해 다음 재귀로
- 다음 재귀 호출 시 남은 개수 1 줄여서 줌

# 1. 테스트 케이스 입력을 받는다. T / N / 연산자 카드 개수 / 연산할 숫자들
# 2. 백트래킹으로 해당 시점에 가능한 계산 경우를 직접 수행하며 계산하는데,
    # 2-1. 만약 모든 연산자 수를 다 썼다면 - MAX 값과 MIN 값 업데이트 후 리턴
    # 2-2. 특정 연산자 카드가 1개 이상이라도 있다면
        # 2-2-1. 인덱스 값 1 올리고, 연산 결과에 해당 연산을 수행하고, 연산자 카드 개수 줄이고 재귀
# 3. MAX - MIN 값 출력. int 형식 주의
"""
from typing import List

# 1. 테스트 케이스 입력을 받는다. T / N / 연산자 카드 개수 / 연산할 숫자들
T: int
N: int
MIN: float = float('inf')
MAX: float = float('-inf')


def backtrack(index: int, result: int, numbers: List, plus: int, minus: int, multiple: int, divide: int) -> None:
    global MIN, MAX

    # 2-1. 만약 모든 연산자 수를 다 썼다면 - MAX 값과 MIN 값 업데이트 후 리턴
    if index == N:  # index == N 이면 연산자 카드 개수를 다 사용한 것임.
        MIN = min(MIN, result)
        MAX = max(MAX, result)
        return

    # 2-2. 특정 연산자 카드가 1개 이상이라도 있다면
    # 2-2-1. 인덱스 값 1 올리고, 연산 결과에 해당 연산을 수행하고, 연산자 카드 개수 줄이고 재귀
    if plus > 0:
        backtrack(index+1, result + numbers[index], numbers, plus-1, minus, multiple, divide)
    if minus > 0:
        backtrack(index+1, result - numbers[index], numbers, plus, minus - 1, multiple, divide)
    if multiple > 0:
        backtrack(index+1, result * numbers[index], numbers, plus, minus, multiple - 1, divide)
    if divide > 0:
        backtrack(index+1, int(result / numbers[index]), numbers, plus, minus, multiple, divide - 1)


def prob_4008() -> None:
    global T, N, MIN, MAX

    T = int(input().strip())
    for tc in range(1, T+1):
        N = int(input().strip())
        MIN = float('inf')
        MAX = float('-inf')

        operators: List[int] = list(map(int, input().split()))
        numbers: List[int] = list(map(int, input().split()))

        # 2. 백트래킹으로 해당 시점에 가능한 계산 경우를 직접 수행하며 계산하는데,
        backtrack(1, numbers[0], numbers, operators[0], operators[1], operators[2], operators[3])

        # 3. MAX - MIN 값 출력. int 형식 주의
        print(f"#{tc} {int(MAX-MIN)}")


if __name__ == "__main__":
    prob_4008()
