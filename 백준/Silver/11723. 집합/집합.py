import sys

S = set()

calculates = int(sys.stdin.readline())

for _ in range(calculates):
    line = sys.stdin.readline().strip().split()
    if len(line) == 1:
        if line[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        cal, x = line[0], line[1]
        x = int(x)
        if cal == 'add':
            S.add(x)
        elif cal == 'remove':
            S.discard(x)
        elif cal == 'check':
            print(1 if x in S else 0)
        elif cal == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
