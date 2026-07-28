def solution(n: int) -> list:
    answer: list = [[0] * _ for _ in range(1, n+1)]     # 삼각형 공간 할당
    x: int = 0  # 초기 x 좌표
    y: int = 0  # 초기 y 좌표
    number = 1  # 초기 숫자
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:          # 아래 방향
                x += 1              # x 좌표 오른쪽
            elif i % 3 == 1:        # 오른쪽 방향
                y += 1              # y 좌표 아래쪽
            elif i % 3 == 2:        # 위쪽 방향
                x -= 1              # x 좌표 왼쪽
                y -= 1              # y 좌표 위쪽
            answer[x-1][y] = number    # 계산을 수행하며 x 좌표가 1 더 많아지므로 -1
            number += 1                # 다음 숫자 할당
    
    # 리스트 comprehension으로 이차원 -> 일차원 리스트 변환
    result = [val for row in answer for val in row]
    return result