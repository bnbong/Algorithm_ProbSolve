A, B = map(str, input().split())
s_A, s_B = A[::-1], B[::-1]
if s_A > s_B:
    print(s_A)
else:
    print(s_B)
    