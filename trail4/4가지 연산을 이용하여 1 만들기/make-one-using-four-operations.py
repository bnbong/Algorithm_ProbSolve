from collections import deque

N = int(input())

# Please write your code here.
# 반대로 생각해서 1을 N으로 만드는 경우를...

def calculate():
    target = 1
    queue = deque([(target, 0)])
    visited = set()
    
    if target == N:
        return 0

    while queue:
        t, dist = queue.popleft()

        for i in range(4):
            if i == 0:
                new_t = t * 3
                if new_t == N:
                    return dist + 1
                if 1 <= new_t <= N + N and new_t not in visited:
                    queue.append((new_t, dist+1))
                    visited.add(new_t)
            elif i == 1:
                new_t = t * 2
                if new_t == N:
                    return dist + 1
                if 1 <= new_t <= N + N and new_t not in visited:

                    queue.append((new_t, dist+1))
                    visited.add(new_t)

            elif i == 2:
                new_t = t + 1
                if new_t == N:
                    return dist + 1
                if 1 <= new_t <= N + N and new_t not in visited:

                    queue.append((new_t, dist+1))
                    visited.add(new_t)

            elif i == 3:
                new_t = t - 1
                if new_t == N:
                    return dist + 1
                if 1 <= new_t <= N + N and new_t not in visited:

                    queue.append((new_t, dist+1))
                    visited.add(new_t)


print(calculate())