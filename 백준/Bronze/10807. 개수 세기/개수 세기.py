N = int(input())
lists = list(map(int, input().split()))
v = int(input())
same = 0

for item in lists:
    if item == v:
        same += 1

print(same)