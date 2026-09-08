"""
SWEA - 1228 암호문 1

암호문 수정 I 명령어로

I x y s => x의 위치 바로 다음에 y개의 숫자를 삽입.
출력은 수정된 결과의 처음 10개 숫자.

원본 암호를 리스트로 선언하면 사이에 값을 넣을 때 나머지 요소들 뒤로 미는 연산이 cost가 좀 클 것 같은데
deque의 insert 함수를 쓰면 될지도?

# 1. 테스트 케이스 입력을 받는다. T / N / 원본 암호문 / 명령어 개수 / 명령어
# 2. 명령어를 파싱한다.
    # 2-0. 인덱스 변수 i를 선언
    # 2-1. insert 함수를 사용하기 위해 명령어셋은 deque로 받는다.
    # 2-2. 리스트 구간을 insert 시 역순으로 하나씩 insert하여 순서 유지(아니면 이중+ 리스트가 됨)
    # 2-3. i를 다음 I 위치로 이동
# 3. 출력한다.
"""
from typing import List, Tuple
from collections import deque


def parse_execute_args(cmds, original: deque):
    # 2-0. 인덱스 변수 i를 선언
    i: int = 0
    while i < len(cmds):
        position: int = int(cmds[i+1])
        additional_encs: int = int(cmds[i+2])
        # 2-2. 리스트 구간을 insert 시 역순으로 하나씩 insert하여 순서 유지(아니면 이중+ 리스트가 됨)
        for item in reversed(cmds[i+3:i+3+additional_encs]):
            original.insert(position, item)
        # 2-3. i를 다음 I 위치로 이동
        i += 3+additional_encs
    return original


def prob_1228() -> None:
    # 1. 테스트 케이스 입력을 받는다. N / 원본 암호문 / 명령어 개수 / 명령어

    for tc in range(1, 11):
        N: int = int(input().strip())
        # 2-1. insert 함수를 사용하기 위해 명령어셋은 deque로 받는다.
        original: deque = deque(list(map(str, input().split())))

        cmd_length: int = int(input().strip())
        cmds: List[str] = list(map(str, input().split()))

        # 2. 명령어를 파싱한다.
        result = list(parse_execute_args(cmds, original))
        # 3. 출력한다.
        print(f"#{tc} {' '.join(result[:10])}")


if __name__ == "__main__":
    prob_1228()
