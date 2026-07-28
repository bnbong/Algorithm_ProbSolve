def solution(elements: list) -> int:
    answer: list = []
    extended = elements * 2                 # 배열을 두 번 이어붙여 원형 배열 처리
    
    for l in range(1, len(elements)+1):     # 부분 수열 길이
        for start in range(len(elements)):
            sub_sum = sum(extended[start:start+l])
            answer.append(sub_sum)
    
    # 중복 제거
    answer = list(set(answer))
    
    return len(answer)