import sys


n = int(sys.stdin.readline())
# 피사노 주기: M=10^k 일 때, k>2 라면, 주기는 항상 15 * 10^(k-1)이다.
mod = 1000000
p = int(mod/10*15)
lists = [0] * (p+1)

def fibo(n):
    lists[0] = 0
    lists[1] = 1

    for i in range(2, p+1):
        lists[i] = lists[i-1] + lists[i-2]
        lists[i] %= mod
    
    return lists[n%p]

print(fibo(n))