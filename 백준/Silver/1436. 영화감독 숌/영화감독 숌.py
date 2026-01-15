T = int(input())

count = 0
devil = 666

while True:
    if '666' in str(devil):
        count += 1
    if count == T:
        break
    devil += 1

print(devil)