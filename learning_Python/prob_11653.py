def factorization(x):
    d = 2

    while d <= x:
        if x % d == 0:
            print(d)
            x = x / d
        else:
            d = d + 1

def prob_11653():
    input_number = int(input())
    result = factorization(input_number)


prob_11653()