N, M = map(int, input().split())

# Please write your code here.
numbers = [i for i in range(1, N+1)]

answer = []

def combination(current_idx, count):
    if count == M:
        print(*answer)
        return
    
    if current_idx == N:
        return

    answer.append(numbers[current_idx])
    combination(current_idx+1, count+1)
    answer.pop()

    combination(current_idx+1, count)

combination(0, 0)
