def prob_5086():
    while True:
        first_num, second_num = map(int, input().split())
        if first_num == second_num == 0: break
        elif first_num % second_num == 0:
            print("multiple")
        elif second_num % first_num == 0:
            print("factor")
        else:
            print("neither")
            

prob_5086()