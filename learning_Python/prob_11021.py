def prob_11021():
    T = int(input())
    for i in range(1, T+1):
        a, b = map(int, input().split())
        print("Case #%d:" %i, a + b)

prob_11021()
    
    # 맞다.. 백준 문제 채점 방식은 input을 한번에 받는 것이 아니라 한 줄 한 줄 입력 받는 것이었다..
    #
    # 삽질의 흔적들.. (reason: indexerror)
    # inputs = list(map(int, input().split()))
    # T, inputs = inputs[0], inputs[1:]
    # # for i in range(T):
    # #     a = i * 2
    # #     b = a + 1
    # #     A, B = inputs[a], inputs[b]
    # #     print("Case #%d:" %(i+1), A + B)
    # i = 0
    # while i < T:   
    #     a = i * 2
    #     b = a + 1
    #     A, B = inputs[a], inputs[b]
    #     print("Case #%d:" %(i+1), A + B)
    #     i += 1