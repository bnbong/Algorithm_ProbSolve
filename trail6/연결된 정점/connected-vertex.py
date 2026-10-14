from collections import Counter

n, m = map(int, input().split())

operations = []
for _ in range(m):
    op, *nums = input().split()
    if op == "x":
        a, b = map(int, nums)
        operations.append((op, a, b))
    else:
        a = int(nums[0])
        operations.append((op, a))

# Please write your code here.

uf = [i for i in range(n+1)]
size = [1] * (n + 1)

def find(x):
    global uf

    if uf[x] == x:
        return x
    
    root_node = find(uf[x])
    uf[x] = root_node

    return root_node


def union(x, y):
    global uf, size

    X = find(x)
    Y = find(y)

    if X != Y:
        uf[X] = Y
        size[Y] += size[X]

for operation in operations:
    op, *nums = operation

    if op == 'x':
        a, b = map(int, nums)
        union(a, b)
    else:
        a = nums[0]
        target = find(a)
        print(size[target])
