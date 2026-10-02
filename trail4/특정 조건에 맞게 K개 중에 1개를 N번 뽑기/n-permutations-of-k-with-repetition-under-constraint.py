K, N = map(int, input().split())

# Please write your code here.
numbers = [i for i in range(1, K+1)]

picked = []

def pick_num(count):

    if count == N:
        print(*picked)
        return

    for i in range(len(numbers)):
        if len(picked) > 1:
            if picked[-1] == picked[-2] == numbers[i]:
                continue
        picked.append(numbers[i])
        curr_num = numbers[i]
        pick_num(count+1)
        picked.pop()


pick_num(0)