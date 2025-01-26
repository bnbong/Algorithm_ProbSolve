T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    counter = 0
    for w in range(1, W+1):
        if counter == N:
            break
        for h in range(1, H+1):
            counter += 1
            if counter == N:
                break
        if counter == N:
            break

    if w < 10:
        print(f"{h}0{w}")
    else:
        print(f"{h}{w}")
