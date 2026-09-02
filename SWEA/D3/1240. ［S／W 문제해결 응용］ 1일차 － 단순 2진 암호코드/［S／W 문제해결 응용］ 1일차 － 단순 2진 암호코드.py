"""
SWEA - 1240 단순 2진 암호코드

숫자를 이진 암호화
0 => 0001101
1 => 0011001
2 => 0010011
3 => 0111101
4 => 0100011
5 => 0110001
6 => 0101111
7 => 0111011
8 => 0110111
9 => 0001011

암호 확인 = (홀수 자리의 숫자들의 합 * 3 + 짝수 자리들의 합) % 10 == 0

이차원 배열로 들어옴
출력은 암호 코드의 8개의 숫자의 합
잘못된 암호 코드인 경우 0

암호 코드의 특징은 맨 끝 숫자는 무조건 1이다(입력으로 들어온 이차원 리스트의 맨 끝 1부터 앞으로 55칸이 암호 부분).
-> 그지같은 입력에서 암호 코드만 추출하는 함수
-> 암호 코드를 숫자로 복호화하는 함수
-> 복호화된 암호 숫자들이 정상인지 확인하는 함수

# 1. 테스트 케이스 입력을 받는다. T / N, M / N * M 크기의 직사각형 배열
# 2. 입력으로 들어온 N * M 배열을 확인한다.
    # 2-1. 하나의 행이 전부 0이면 continue
    # 2-2. 하나의 행에서 1이 확인되면 그 행만 확인 (나머지 아래 행들은 모두 동일하기 때문)
        # 2-2-1. 그 행의 맨 마지막에 나오는 1의 위치부터 앞으로 55번째 칸을 암호 구간으로 추출
            # 2-2-1-1. 7칸씩 슬라이싱
        # 2-2-2. 암호 구간을 10진수 숫자로 복호화
        # 2-2-3. 복호화된 숫자가 정상인지 확인
# 3. 암호 확인이 끝나면 복호화된 10진수 숫자 합을 출력(암호 틀리면 0)
"""
from typing import List, Tuple


PW_TABLE = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}


def check_decoded(numbers: List[int]) -> Tuple[bool, int]:
    # 2-2-3. 복호화된 숫자가 정상인지 확인
    sum_of_holsu: int = sum(numbers[i] for i in range(0, 8, 2))
    sum_of_jjaksu: int = sum(numbers[i] for i in range(1, 8, 2))

    result: int = sum_of_holsu*3+sum_of_jjaksu

    return result % 10 == 0, sum(numbers)


def decode_target(target: str) -> List[int]:
    result: List[int] = []
    # 2-2-1-1. 7칸씩 슬라이싱
    sliced = [target[i:i+7] for i in range(0, len(target), 7)]

    # 2-2-2. 암호 구간을 10진수 숫자로 복호화
    for item in sliced:
        result.append(PW_TABLE[item])

    return result


def check_code(code: str) -> Tuple[bool, int]:
    reversed_code = code[::-1]
    index_of_1 = reversed_code.find('1')
    if index_of_1 != -1:
        return True, index_of_1
    return False, index_of_1


def solve() -> None:
    # 1. 테스트 케이스 입력을 받는다. T / N, M / N * M 크기의 직사각형 배열
    T: int = int(input().strip())

    for tc in range(1, T+1):
        N, M = map(int, input().split())
        answer: int = 0
        detected: bool = False
        for _ in range(N):
            # 2. 입력으로 들어온 N * M 배열을 확인한다.
            code: str = input().strip()
            if detected:
                continue

            detected, index_of_1 = check_code(code)  # index_of_1은 뒤집은 상태의 인덱스이므로
            if not detected:
                # 2-1. 하나의 행이 전부 0이면 continue
                continue
            # 2-2. 하나의 행에서 1이 확인되면 그 행만 확인 (나머지 아래 행들은 모두 동일하기 때문)
            index_of_1 = len(code) - index_of_1 - 1  # 원래의 앞쪽부터 읽는 인덱스로 변환

            # 2-2-1. 그 행의 맨 마지막에 나오는 1의 위치부터 앞으로 55번째 칸을 암호 구간으로 추출
            target: str = code[index_of_1-55:index_of_1+1]
            result: List[int] = decode_target(target)

            check, _answer = check_decoded(result)
            if check:  # 암호가 정상인 경우에만 answer 업데이트
                answer = _answer

        # 3. 암호 확인이 끝나면 복호화된 10진수 숫자 합을 출력(암호 틀리면 0)
        print(f"#{tc} {answer}")


if __name__ == "__main__":
    solve()
