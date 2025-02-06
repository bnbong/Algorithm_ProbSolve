import sys

input = sys.stdin.readline

N = int(input())
x_list = list(map(int, input().split()))

sorted_1 = sorted(list(set(x_list)))

comp = dict(zip(sorted_1, list(range(len(sorted_1)))))  # 새롭게 알게 된 함수, zip - 인덱스 매핑
for item in x_list:
    print(comp[item], end=' ')