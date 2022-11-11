def gcd(A, B):
    if B == 0: return A
    else: return gcd(B, A % B)

def prob_1934():
    test_cases = int(input())
    results = []

    for i in range(0, test_cases):
        A, B = map(int, input().split())
        multiplied_AB = A * B
        A = gcd(A, B)
        
        lcm = multiplied_AB / A
        results.append(round(lcm))

    for result in results:
        print(result)
    

prob_1934()