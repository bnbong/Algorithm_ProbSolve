namoji = []

for _ in range(10):
    namo_number = int(input()) % 42
    namoji.append(namo_number)

print(len(set(namoji)))
