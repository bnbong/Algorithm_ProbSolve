def check_same_o(string):
    result = 0
    same_o = 0

    for i in range(len(string)):
        if string[i] == 'O':
            same_o += 1
            result += same_o
        else:
            same_o = 0
            
    print(result)

def prob_8958():
    test_cases = int(input())

    for i in range(test_cases):
        string = list(str(input()))
        check_same_o(string)
        
prob_8958()