# failed via time limits
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1

#     return fibo(n - 1) + fibo(n - 2)

# def prob_2748():
#     n = int(input())
#     result = 0
#     result = fibo(n)

#     print(result)

def prob_2748():
    n = int(input())
    fibo = []
    num = 0
    for i in range(n + 1):
        if i == 0:
            num = 0
        elif i <= 2:
            num = 1
        else:
            num = fibo[-1] + fibo[-2]
        fibo.append(num)

    print(fibo[-1])

prob_2748()