# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")
from typing import List


def rotate_90(number_array: List, N: int) -> List:
    # 2-1. 90도 회전이면, 행 인덱스를 열 인덱스로 바꾸고 열 인덱스를 (전체 행 길이 - 현재 행)으로 변경.
    result_90: List = [[0] * N for _ in range(N)]            # 결과를 저장할 새 리스트 선언(크기 통일)
    for i in range(N):
        for j in range(N):
            result_90[j][N-1-i] = number_array[i][j]         # N-1로 해줘야 인덱스에 맞출 수 있음

    return result_90



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T+1):
        N: int = int(input().strip())                                   # N 입력
        number_array: List = []
        for _ in range(N):                                              # NxN 행렬 입력
            number_array.append(list(map(str, input().split())))        # 요소를 str로 받아 최종적으로 문자열로 합침

        # 2. 행렬의 회전한 모습을 담는다.
        array_90 = rotate_90(number_array=number_array, N=N)
        array_180 = rotate_90(number_array=array_90, N=N)
        array_270 = rotate_90(number_array=array_180, N=N)

        # 3. 회전한 행렬을 출력한다(첫 번째 열 = 90도 회전 / 두 번째 열 = 180도 회전 / 세 번째 열 = 270도 회전)
        print(f"#{tc}")
        for i in range(N):
            print(''.join(array_90[i]), ''.join(array_180[i]), ''.join(array_270[i]))

