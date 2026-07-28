def solution(want: list, number: list, discount: list) -> int:
    answer: int = 0
    junghyeon: dict = dict(zip(want, number))   # want, number 리스트 개수가 같으므로 zip 함수로 묶어서 dict로 변환
    
    window_len: int = sum(n for n in number)
    
    # 할인 목록의 길이가 원하는 기간보다 짧으면 0 리턴
    if len(discount) < window_len:
        return 0
    
    
    # 첫 번째 윈도우
    mart: dict = {}
    for j in range(window_len):
        item = discount[j]
        mart[item] = mart.get(item, 0) + 1
    
    # 첫 번째 윈도우 비교
    if mart == junghyeon:
        answer += 1
        
    # 윈도우 이동
    for i in range(len(discount) - window_len):
        # 이전 윈도우 첫 요소 제거
        left_item = discount[i]
        mart[left_item] -= 1
        if mart[left_item] == 0:
            del mart[left_item] # 요소 자체를 제거
            
        # 새 요소 추가
        right_item = discount[i + window_len]
        mart[right_item] = mart.get(right_item, 0) + 1
        
        # 비교
        if mart == junghyeon:
            answer += 1
    
    return answer