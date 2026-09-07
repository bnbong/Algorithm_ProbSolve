"""
SWEA - 1218 괄호 짝짓기

stack으로 처리하는게 깔끔할듯

# 1. 테스트 케이스 입력을 받는다. T / 테케 길이 / 테케 문자열
# 2. 브라켓을 담을 스택을 선언한다.
# 3. 시작하는 브라캣이라면 스택에 담고
# 4. 닫는 브라캣이라면 스택에서 꺼내는데, 스택에서 꺼낸 것의 매핑과 읽고 있는 인풋이 같지 않다면 0
# 5. 스택 다 돌았는데도 문제 없으면 1
"""
from typing import List, Dict


BRACKET: Dict = {  # 괄호 짝을 매핑하는 딕셔너리.
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>',
}
# 1. 테스트 케이스 입력을 받는다. 테케 길이 / 테케 문자열


def solve() -> None:

    for tc in range(1, 11):
        length: int = int(input().strip())
        brackets: List[str] = list(map(str, input()))

        # 2. 브라켓을 담을 스택을 선언한다.
        stacks: List[str] = []
        result: int = 1

        for b in brackets:
            # 3. 시작하는 브라캣이라면 스택에 담고
            if b in ['{', '[', '(', '<']:
                stacks.append(b)
            # 4. 닫는 브라캣이라면 스택에서 꺼내는데, 스택에서 꺼낸 것의 매핑과 읽고 있는 인풋이 같지 않다면 0
            else:
                if len(stacks) <= 0:
                    result = 0
                    break
                target = stacks.pop()
                if BRACKET[target] != b:
                    result = 0

        if len(stacks) != 0:
            result = 0

        # 5. 스택 다 돌았는데도 문제 없으면 1
        print(f"#{tc} {result}")


if __name__ == "__main__":
    solve()
