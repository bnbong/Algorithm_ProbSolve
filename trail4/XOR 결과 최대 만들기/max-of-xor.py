n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

picked = []

max_number = -1

def pick_number(curr_idx):
    global max_number, picked

    if len(picked) == m:
        _temp = 0
        for item in picked:
            _temp ^= item

        max_number = max(max_number, _temp)
        return
    
    if curr_idx >= len(A):
        return
    
    picked.append(A[curr_idx])
    pick_number(curr_idx + 1)
    picked.pop()

    pick_number(curr_idx + 1)

    return

pick_number(0)
print(max_number)