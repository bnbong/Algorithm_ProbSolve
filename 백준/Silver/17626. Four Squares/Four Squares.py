import math


def laglangdu(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return True
    else:
        return False


n = int(input())

counter = 4

if laglangdu(n):  # 그냥 제곱수인 경우
    counter = 1
else:
    for i in range(int(math.sqrt(n)), 0, -1):
        if laglangdu(n - i**2):  # 두 개의 제곱수로 이루어진 경우
            counter = 2
            break
        else:
            for j in range(int(math.sqrt(n-i**2)), 0, -1):
                if laglangdu((n - i**2 - j**2)):  # 3개의 제곱수로 이루어진 경우
                    counter = 3
                    break

print(counter)
