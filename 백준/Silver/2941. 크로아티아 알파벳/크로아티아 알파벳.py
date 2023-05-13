# sentence = list(input())
# result = len(sentence)

# for i in range(len(sentence)):
#     if sentence[i] == 'j' and i != 0:
#         if sentence[i-1] == 'l' or sentence[i-1] == 'n':
#             result -= 1
#     elif sentence[i] == '=':
#         if sentence[i-1] == 's' or sentence[i-1] == 'z' or sentence[i-1] == 'c':
#             if sentence[i-2] == 'd':
#                 result -= 1
#             result -= 1
#     elif sentence[i] == '-':
#         if sentence[i-1] == 'c' or sentence[i-1] == 'd':
#             result -= 1

# print(result)

croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
sentence = input()

for alphabet in croatia_alphabet:
    sentence = sentence.replace(alphabet, 'C')

print(len(sentence))