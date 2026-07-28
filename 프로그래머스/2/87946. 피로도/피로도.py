from itertools import permutations

def solution(k: int, dungeons: list[list]) -> int:
    answer: int = -1
    
    for i in permutations(dungeons, len(dungeons)): # 던전의 개수가 최대 8개, 적은 편이므로 순열을 사용해서 최대 던전 수 계산
        temp: int = k   # 피로도 계산
        count: int = 0  # 갈 수 있는 던전 수
        
        for piro, somo in i:    # 각 던전 순서 조합을 바탕으로 최대로 갈 수 있는 던전 수 계산
            if temp >= piro:    # 현재 피로도가 요구 피로도보다 높다면
                temp -= somo    # 현재 피로도 - 소모 피로도
                count += 1      # 던전 수 +1
        
        answer = max(count, answer) # 순회하며 가장 많이 갈 수 있는 던전 수 최대값 계산

    return answer