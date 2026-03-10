N = int(input())

result = 0

def find_generator(N):
    global result

    for i in range(N):
        sum = i
        for j in str(i):
            sum += int(j)
        if sum == N:
            result = i
            break
    
    return result

find_generator(N)

print(result)
