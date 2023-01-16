def prob_2506():
    n = int(input())
    problems = list(map(int, input().split()))
    sums = 0
    result = 0

    for i in range(len(problems)):
        if problems[i] == 1:
            sums += 1
            result += sums
        else:
            sums = 0

    print(result)

prob_2506()
 