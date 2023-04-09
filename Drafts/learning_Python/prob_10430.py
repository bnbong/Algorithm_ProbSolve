def prob_10430():
    A, B, C = map(int, input().split())
    print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*((B%C))%C), sep="\n")

prob_10430()