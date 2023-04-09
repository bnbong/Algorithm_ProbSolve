def prob_5355():
    cases = int(input())
    results = []

    for case in range(0, cases):
        calculate = input().split(" ")
        
        number = float(calculate[0])
        calculate = calculate[1:]

        for item in calculate:
            if item == "@":
                number = number * 3.00
            if item == "%":
                number = number + 5.00
            if item == "#":
                number = number - 7.00
        
        results.append(number)

    for number in results:
        print(format(round(number, 2), ".2f"))

prob_5355()