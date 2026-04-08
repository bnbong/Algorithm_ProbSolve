import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

my_deque = deque()

for _ in range(N):
    command = list(map(str, input().split()))

    if command[0] == "push_front":
        my_deque.appendleft(command[1])
    elif command[0] == "push_back":
        my_deque.append(command[1])
    elif command[0] == "pop_front":
        try:
            print(my_deque.popleft())
        except IndexError:
            print(-1)
    elif command[0] == "pop_back":
        try:
            print(my_deque.pop())
        except IndexError:
            print(-1)
    elif command[0] == "size":
        print(len(my_deque))
    elif command[0] == "empty":
        if len(my_deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        try:
            print(my_deque[0])
        except IndexError:
            print(-1)
    elif command[0] == "back":
        try:
            print(my_deque[-1])
        except IndexError:
            print(-1)
