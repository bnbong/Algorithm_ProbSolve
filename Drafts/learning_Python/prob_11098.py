def prob_11098():
    test_cases = int(input())

    for _ in range(test_cases):
        people = int(input())
        people_list = []

        for _ in range(people):
            price, name = map(str, input().split())
            people_list.append([int(price), name])

        people_list = sorted(people_list, key=lambda x: x[0])
        print(people_list[-1][1])

prob_11098()