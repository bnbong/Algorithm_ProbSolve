def prob_11557():
    test_cases = int(input())

    for i in range(test_cases):
        number_of_schools = int(input())
        result = []

        for _ in range(number_of_schools):
            school, liter = map(str, input().split())
            result.append([school, int(liter)])
        
        result = sorted(result, key=lambda x: x[1])
        print(result[-1][0])

prob_11557()