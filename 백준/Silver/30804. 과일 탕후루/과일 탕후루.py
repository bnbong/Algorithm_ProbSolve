import sys

input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))

start = 0
end = 0
count = dict()
distincts = 0
ans = 0

for end in range(N):
    if fruits[end] in count:  # 투 포인터 중 우측의 포인터를 1씩 늘려가며 탐색
        count[fruits[end]] += 1
    else:
        count[fruits[end]] = 1
        distincts += 1

    while distincts > 2:  # 과일이 2종류 이상이면
        count[fruits[start]] -= 1  # 해당 과일 넘버의 과일 하나를 탕후루에서 뺌
        if count[fruits[start]] == 0:  # 해당 과일 넘버의 과일이 다 빠지면
            del count[fruits[start]]
            distincts -= 1  # 과일 종류 카운터를 하나 줄이고
        start += 1  # 투 포인터 중 좌측의 포인터를 1 늘림

    ans = max(ans, end - start + 1)  # for loop 시행 당 ans 값 중 더 큰 쪽을 업데이트

print(ans)
