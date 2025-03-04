import sys
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    m = 0
    n = 0
    result = x
    __final = math.lcm(M, N)

    while result <= __final:
        if (result - 1) % N + 1 == y:
            break
        result += M
    
    if result > __final:
        print(-1)
    else:
        print(result)
