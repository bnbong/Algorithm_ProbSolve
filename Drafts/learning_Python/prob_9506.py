def prob_9506():
    while True:
        test_number = int(input())
        if test_number == -1: break
        result = []
        for i in range(1, test_number):
            if test_number % i == 0:
                result.append(i)
        
        if sum(result) == test_number:
            print(test_number, "=", " + ".join(str(j) for j in result))
        else:
            print(test_number, "is NOT perfect.")

prob_9506()