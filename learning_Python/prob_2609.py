def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

def prob_2609():
    A, B = map(int, input().split())
    gcd_result = 0
    gcd_result = gcd(A, B)
    lcm = A * B / gcd_result
    print(gcd_result, round(lcm), sep='\n')

prob_2609()