word = 'Monty Python'

print(word[:5])
print(word[5:])
print(word[6:-2])
print(word[10:5])
print(word[-3:-5])
print(word[2:10:3])
print(word[10:5:-2])

_str = input("문자열을 입력하시오: ")
first = _str[0:2]
last = _str[-2:]
print(f"출력화면: {first+last}")
