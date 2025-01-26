while True:
    A, B, C = map(int, input().split())
    if A == B == C == 0:
        break
    tri = [A, B, C]
    bit_beon = max(A, B, C)
    tri.remove(bit_beon)

    _sum = 0
    for item in tri:
        _sum += item**2
    if _sum == bit_beon**2:
        print("right")
    else:
        print("wrong")
