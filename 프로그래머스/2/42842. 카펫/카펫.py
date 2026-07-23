def get_yaksu(n):
    yak = []
    i=1
    while i <= n//i:
        if n % i == 0:
            yak.append((n//i, i))
        i += 1
    return yak

def solution(brown, yellow):
    answer = []
    n = brown + yellow
    yak = get_yaksu(n)
    
    for a, b in yak:
        if (a - 2) * (b - 2) == yellow:
            answer = [a, b]

    return answer