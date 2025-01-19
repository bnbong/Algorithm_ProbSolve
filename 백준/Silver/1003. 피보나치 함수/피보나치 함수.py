import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    zero = 1
    one = 0
    for _ in range(n):
        zero, one = one, zero+one
    print(zero, one)
