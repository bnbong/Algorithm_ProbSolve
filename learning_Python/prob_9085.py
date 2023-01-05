def prob_9085():
    T = int(input())
    for i in range(T):
        n = int(input())
        numbers = list(map(int, input().split()))
        print(sum(numbers))

prob_9085()
