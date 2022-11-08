def prob_1789():
    sum_of_number = int(input())
    n = 1

    while n * (n + 1) / 2 <= sum_of_number:
        n += 1
    
    print(n - 1)

prob_1789()