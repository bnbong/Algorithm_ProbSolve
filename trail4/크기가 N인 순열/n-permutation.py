n = int(input())

# Please write your code here.
numbers = [i for i in range(1, n+1)]
visited = [False for _ in range(n)]

picked = []

def pick_number():
    if len(picked) == len(numbers):
        print(*picked)
        return

    for i in range(n):
        if visited[i] == True:
            continue
        picked.append(numbers[i])
        visited[i] = True
        pick_number()
        visited[i] = False
        picked.pop()

pick_number()
