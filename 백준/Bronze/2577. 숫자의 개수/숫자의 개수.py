A = int(input())
B = int(input())
C = int(input())
result = A*B*C
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

result = str(result)
for num in nums:
    print(result.count(num))

