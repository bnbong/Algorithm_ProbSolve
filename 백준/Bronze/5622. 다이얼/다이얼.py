string = input()
dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for i in string:
    for j in dials:
        if i in j:
            result += dials.index(j) + 3

print(result)
