def prob_10988():
    sentence = str(input())

    result = 1
    i = 0
    while not i >= len(sentence) - i:
        if sentence[i] != sentence[len(sentence) - i - 1]:
            result = 0 
        i += 1

    print(result)

prob_10988()