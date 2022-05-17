def prob_2588():
    A = int(input())
    B = int(input())

    n5, n4, n3 = [int(a) for a in str(B)]
    N3, N4, N5 = A*n3, A*n4, A*n5
    print(N3, N4, N5, N3 + N4*10 + N5*100, sep="\n")

prob_2588()