def prob_11022():
    T = int(input())
    for i in range(1, T+1):
        a, b = map(int, input().split())
        # print("Case #%d: %d + %d = " %(i, a, b), a + b) 같은 결과를 내지만 채점 중 출력형식이 잘못되었다는 오류 발생.
        print(f'Case #{i}: {a} + {b} = {a+b}')

prob_11022()