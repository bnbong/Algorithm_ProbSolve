def prob_10102():
    people = int(input())
    voted = str(input())

    a_count = voted.count('A')
    b_count = voted.count('B')

    if a_count == b_count:
        print("Tie")
    elif a_count > b_count:
        print("A")
    else:     
        print("B")

prob_10102()