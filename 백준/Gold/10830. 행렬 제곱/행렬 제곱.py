N, B = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]

def multiple_vector(V1, V2):
    n = len(V1)
    result_vector = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            element = 0
            for i in range(n):
                element += V1[row][i] * V2[i][col]
            
            result_vector[row][col] = element % 1000

    return result_vector

def split_vector(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
        
    tmp = split_vector(A, B//2)
    if B % 2:
        return multiple_vector(multiple_vector(tmp, tmp), A)
    else:
        return multiple_vector(tmp, tmp)
    
result = split_vector(A, B)

for element in result:
    print(*element)
