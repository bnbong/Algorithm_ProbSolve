sentences_num = int(input())
group_num = sentences_num

for _ in range(sentences_num):
    sentence = input()
    for i in range(len(sentence) - 1):
        _current = sentence.index(sentence[i])
        _next = sentence.index(sentence[i+1])
        if _current > _next:
            group_num -= 1
            break

print(group_num)
