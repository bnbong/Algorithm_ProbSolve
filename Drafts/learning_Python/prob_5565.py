def prob_5565():
    sum_of_book = int(input())
    result = 0
    for _ in range(9):
        price_of_book = int(input())
        result += price_of_book
    
    result = sum_of_book - result
    print(result)


prob_5565()