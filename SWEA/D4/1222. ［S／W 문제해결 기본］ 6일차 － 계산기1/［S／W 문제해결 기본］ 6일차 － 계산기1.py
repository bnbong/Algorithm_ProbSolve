"""
SWEA - 1222 계산기 1

입력값을 다 받으면
계산식을 순회하면서 이를 후위표기식으로 바꾼 뒤
후위표기식을 바탕으로 요소를 읽으면서 숫자 요소들은 스택에 push.
연산자 만나기 전까지는 stack에 숫자가 2개 있을 것임.
연산자 만나면 pop 두 번 후 두 값 더해서 스택에 push.
다 돌고 stack에 남아 있는 값이 결과

후위 표기식은 홀수번 인덱스에 숫자가 있고 짝수번 인덱스에 연산자가 있음.
expression[0] expression[1] expression[2]


# 1. 테스트 케이스 입력을 받는다.

"""
from typing import List

L: int


def make_postorder(expression: List[str]) -> List[str]:
    postorder_stack: List[str] = [expression[0]]

    for i in range(1, len(expression)):
        if expression[i] == '+':
            continue
        else:
            postorder_stack.append(expression[i])
            postorder_stack.append(expression[i-1])

    return postorder_stack


def calculate(L: int, postorder_stack: List[str]) -> int:
    result_stack: List[int] = []
    for i in range(L):
        if postorder_stack[i] == '+':
            a: int = result_stack.pop()
            b: int = result_stack.pop()
            result_stack.append(a+b)
        else:
            result_stack.append(int(postorder_stack[i]))

    return int(result_stack[0])


def solve() -> None:
    global L


    for tc in range(1, 11):
        L = int(input().strip())
        expression: List[str] = list(map(str, input().strip()))

        postorder_stack: List[str] = make_postorder(expression)
        result: int = calculate(L, postorder_stack)

        print(f"#{tc} {result}")


if __name__ == "__main__":
    solve()
