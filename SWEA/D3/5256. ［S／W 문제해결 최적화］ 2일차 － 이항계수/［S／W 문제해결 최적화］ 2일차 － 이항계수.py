"""
x^a*y^b의 계수를 구해야함

nCb
"""
import math


def comb(n, k):
    if k < 0 or k > n:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def prob_5256():
    T: int = int(input().strip())

    for tc in range(1, T+1):
        n, a, b = map(int, input().split())

        print(f"#{tc} {comb(n, b)}")


if __name__ == "__main__":
    prob_5256()
