import sys

input = sys.stdin.readline

N = int(input())

queue = []

for _ in range(N):
    inst = list(map(str, input().split()))

    if len(inst) == 2:
        queue.append(int(inst[1]))

    if inst[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            target = queue[0]
            print(target)
            queue.remove(target)

    elif inst[0] == "size":
        print(len(queue))

    elif inst[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif inst[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif inst[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
