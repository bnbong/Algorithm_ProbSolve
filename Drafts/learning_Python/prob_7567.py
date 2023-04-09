def prob_7567():
    dishes = list(str(input()))
    length = 0

    for i in range(len(dishes)):
        if i == 0:
            length += 10
        elif dishes[i] == dishes[i - 1]:
            length += 5
        else:
            length += 10

    print(length)

prob_7567()