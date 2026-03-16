from sys import stdin

N = int(stdin.readline())

sort = []

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])
    return merge(left_half, right_half)

for i in range(N):
    sort.append(int(stdin.readline()))

solve = mergesort(sort)
for i in solve:
    print(i)