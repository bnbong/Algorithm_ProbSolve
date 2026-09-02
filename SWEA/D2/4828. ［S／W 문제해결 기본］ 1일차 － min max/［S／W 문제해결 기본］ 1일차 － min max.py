"""
요소 순회하면서 요소 비교를 통해 더 큰 요소를 저장해서 max 요소를 / 더 작은 요소를 min 요소로 저장해서
차이를 구하는건가 
"""
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())                    # 양수의 개수 N
    numbers = []                        # N개의 양수 a_i
    for num in input().split():
        numbers.append(int(num))
    # numbers = list(map(int, input().split())) 을 써도 될 것 같은데 강의에서는 익숙함에 주의하라고 함
    max_value, min_value = numbers[0], numbers[0]
    for i in range(len(numbers)):
        if max_value < numbers[i]:
            max_value = numbers[i]
        
        if min_value > numbers[i]:
            min_value = numbers[i]
    
    print(f"#{test_case} {max_value - min_value}")
