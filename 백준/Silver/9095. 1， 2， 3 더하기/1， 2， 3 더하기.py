# 1 : 1 => 1개
# 2 : 1+1 / 2 => 2개
# 3 : 1+1+1 / 1+2 / 2+1 / 3 => 4개
T = int(input())

t = [0] * 11
t[0] = 1
t[1] = 2
t[2] = 4

for i in range(3, len(t)):
    t[i] = t[i-1] + t[i-2] + t[i-3]


for i in range(T):
    n = int(input())
    print(t[n-1])
