def prob_10569():
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().split())
        print(2 - V + E)

prob_10569()
