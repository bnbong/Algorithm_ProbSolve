string = input()
result = []
for i in range(len(string)):
    if string[i].islower():
        result.append(string[i].upper())
    else:
        result.append(string[i].lower())

for item in result:
    print(item, end='')
