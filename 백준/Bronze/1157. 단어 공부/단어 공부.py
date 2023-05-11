sentence = input().lower()
sentence_alphabet = list(set(sentence))

counters = []

for alphabet in sentence_alphabet:
    cnt = sentence.count(alphabet)
    counters.append(cnt)

if counters.count(max(counters)) >= 2:
    print("?")
else:
    print(sentence_alphabet[(counters.index(max(counters)))].upper())
