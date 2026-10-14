n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]

uf = [i for i in range(n+1)]
# Please write your code here.

def find(x):
    global uf

    if uf[x] == x:
        return x
    
    root_node = find(uf[x])
    uf[x] = root_node

    return root_node    


def union(x, y):
    global uf
    X = find(x)
    Y = find(y)
    uf[X] = Y

for q in query:
    check, a, b = q
    if check == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print(1)
        else:
            print(0)