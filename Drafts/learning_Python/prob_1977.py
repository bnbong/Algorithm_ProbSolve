def prob_1977():
    n = int(input())
    m = int(input())

    number = 1
    perfect_multiple = []
    
    while number ** 2 <= m:
        if n <= number ** 2 <= m:
            perfect_multiple.append(number ** 2)
        number += 1
    
    if len(perfect_multiple) != 0:
        print(sum(perfect_multiple))
        print(perfect_multiple[0])
    else:
        print(-1)

prob_1977()