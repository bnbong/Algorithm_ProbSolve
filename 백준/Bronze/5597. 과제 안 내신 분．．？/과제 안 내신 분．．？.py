max_list = [i for i in range(1, 31)]

for _ in range(28):
    student_number = int(input())
    max_list.remove(student_number)

print(min(max_list))
print(max(max_list))
