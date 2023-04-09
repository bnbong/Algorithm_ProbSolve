def check_stick(times):
    if times.count(0) == 0:
        print('E')
    elif times.count(0) == 1:
        print('A')
    elif times.count(0) == 2:
        print('B')
    elif times.count(0) == 3:
        print('C')
    elif times.count(0) == 4:
        print('D')
    
    

def prob_2490():
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    third = list(map(int, input().split()))

    check_stick(first)
    check_stick(second)
    check_stick(third)

prob_2490()
