import sys

input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
        keywords = list(map(str, input().split()))
        
        if len(keywords) != 1:
            stack.append(int(keywords[1]))
            
        if keywords[0] == "top":
            try:
                print(stack[-1])
            except IndexError:
                print(-1)
        elif keywords[0] == "size":
            print(len(stack))
        elif keywords[0] == "pop":
            try:
                output = stack[-1]
                print(output)
                stack.reverse()
                stack.remove(output)
                stack.reverse()
            except IndexError:
                print(-1)
        elif keywords[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)