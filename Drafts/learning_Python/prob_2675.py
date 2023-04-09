def repeat_string(repeat_time, string):
    result_string = ""
    for i in range(0, len(string)):
        result_string += string[i] * repeat_time

    return result_string

def prob_2675():
    test_limits = int(input())
    results = []
    
    for case in range(0, test_limits):
        repeat_time, string = input().split(" ")
        repeat_time = int(repeat_time)
        new_string = repeat_string(repeat_time, string)
        results.append(new_string)
    
    for result in results:
        print(result)

prob_2675()