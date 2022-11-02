def prob_2935():
    first_number = int(input())
    operator = input()
    second_number = int(input())

    result = 0
    if operator == "*":
        result = first_number * second_number
    else:
        result = first_number + second_number

    print(result)


prob_2935()