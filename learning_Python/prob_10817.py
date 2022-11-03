def prob_10817():
    number_list = []
    number_1, number_2, number_3 = map(int, input().split())
    number_list.append(number_1)
    number_list.append(number_2)
    number_list.append(number_3)
    number_list.sort()

    print(number_list[1])

prob_10817()