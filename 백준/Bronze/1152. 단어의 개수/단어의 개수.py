sentence = list(input().split(' '))

words = 0
for w in sentence:
        if w == '':
                continue
        words += 1

print(words)