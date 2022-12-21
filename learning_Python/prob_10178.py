def prob_10178():
    N = int(input())
    for _ in range(N):
        c, v = map(int, input().split())
        you = c // v
        dad = c % v
        print("You get", you, "piece(s) and your dad gets", dad, "piece(s).")

prob_10178()
