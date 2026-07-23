import math


def solution(clothes):
    answer = 0
    
    cony = {}
    for cloth in clothes:
        if cloth[1] not in cony:
            cony[cloth[1]] = []
        cony[cloth[1]].append(cloth[0])
    hubo = []
    for item in cony.values():
        hubo.append(len(item))

    result = 1
    for h in hubo:
        result *= (h+1)
    answer = result - 1

    return answer