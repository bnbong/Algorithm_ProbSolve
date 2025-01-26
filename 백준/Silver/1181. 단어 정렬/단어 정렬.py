T = int(input())

result = dict()

for _ in range(T):
    string = input()
    if len(string) in result:
        result[len(string)].append(string)
    else:
        result[len(string)] = [string]

sorted_1 = list(dict(sorted(result.items())).values())
sorted_2 = []
for item in sorted_1:
    if len(item) > 1:
        item = list(set(item))
        item.sort()
        for inner_item in item:
            sorted_2.append(inner_item)
    else:
        sorted_2.append(item.pop())

for i in sorted_2:
    print(i)
