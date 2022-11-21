def prob_5717():
    while True:
        boy, girl = map(int, input().split())
        if boy == girl == 0: break
        else:
            print(boy + girl)

prob_5717()