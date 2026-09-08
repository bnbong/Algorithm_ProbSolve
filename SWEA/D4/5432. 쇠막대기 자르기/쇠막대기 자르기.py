"""
SWEA - 5432 쇠막대기 자르기

레이저는 괄호 완성체 ()로 표기
쇠막대기 왼쪽 끝은 (, 오른쪽 끝은 )

쇠막대기 내부에 레이저 개수 + 1 한 값이 레이저로 잘린 조각임

1. (를 만났을 때:
    쇠막대기의 시작일 수도, 레이저의 시작일 수도 있으므로 일단 스택에 append('(') 합니다.

2. )를 만났을 때 (2가지 경우):
    Case A: 바로 전 문자가 (인 경우 (레이저 발사!)
        스택에서 pop()하여 레이저 괄호를 제거합니다.
        핵심: 레이저가 발사되었으므로, 현재 스택에 남아있는 (의 개수(=현재 겹쳐있는 쇠막대기 수)만큼 조각(result)에 더합니다.
    Case B: 바로 전 문자가 )인 경우 (쇠막대기의 끝!)
        쇠막대기 하나가 끝났으므로 스택에서 pop()합니다.
        막대기가 끝날 때 마지막 잘린 조각 1개가 추가되므로 result += 1을 해줍니다.

# 1. 테스트 케이스 입력을 받는다.
# 2. 쇠파이프 개수를 담는 변수를 만든다.
# 3. 스택을 하나 선언한다.
# 4. brackets 인덱스 0부터 돈다.
    # 4-1. '('를 만나면 스택에 push
    # 4-2. ')'를 만나면
        # 4-3. [레이저] 스택에 pop한 문자가 (라면 현재 스택에 있는 (의 개수만큼 result에 더함, (개수가 쇠막대기 수임
        # 4-4. [막대기 끝] 스택에 pop한 문자가 )라면 result += 1 (마지막 잘린 조각 1개가 추가되기 때문)
"""
from typing import List


brackets: List[str]
result: int
stacks: List[str]


def input_testcase() -> None:
    global brackets
    brackets = []
    brackets = list(input().strip())


def make_iron_pipes() -> None:
    global brackets, result, stacks

    # 4. brackets 인덱스 0부터 돈다.
    for i in range(len(brackets)):
        # 4-1. '('를 만나면 스택에 push
        if brackets[i] == '(':
            stacks.append(brackets[i])
        # 4-2. ')'를 만나면
        else:
            stacks.pop()
            # 4-3. [레이저] 스택에 pop한 문자가 (라면 현재 스택에 있는 (의 개수만큼 result에 더함, (개수가 쇠막대기 수임
            if brackets[i - 1] == '(':
                result += len(stacks)
            # 4-4. [막대기 끝] 스택에 pop한 문자가 )라면 result += 1 (마지막 잘린 조각 1개가 추가되기 때문)
            else:
                result += 1


def prob_5432() -> None:
    global brackets, result, stacks

    T: int = int(input().strip())

    for tc in range(1, T+1):
        # 1. 테스트 케이스 입력을 받는다.
        input_testcase()

        # 2. 쇠파이프 개수를 담는 변수를 만든다.
        result = 0
        # 3. 스택을 하나 선언한다.
        stacks = []

        make_iron_pipes()

        print(f"#{tc} {result}")


if __name__ == "__main__":
    prob_5432()
