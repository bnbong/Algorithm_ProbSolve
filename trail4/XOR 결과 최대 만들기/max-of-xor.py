n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

answer = []
result = []

def combination(current_idx, count):
    if count == m:
        _temp = 0
        for item in answer:
            _temp ^= item
        result.append(_temp)
        return
    
    if current_idx == n:
        return

    answer.append(A[current_idx])
    combination(current_idx+1, count+1)
    answer.pop()

    combination(current_idx+1, count)

combination(0, 0)

print(max(result))