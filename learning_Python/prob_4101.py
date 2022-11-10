def prob_4101():
    results = []
    yes_string = 'Yes'
    no_string = 'No'
    while True:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break;
        elif A > B:
            results.append(yes_string)
        else:
            results.append(no_string)

    for result in results:
        print(result)

prob_4101()