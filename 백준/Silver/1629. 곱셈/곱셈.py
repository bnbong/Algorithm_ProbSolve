A, B, C = map(int, input().split())

def split_vector(A, B):
    if B == 1:
        return A % C
        
    tmp = split_vector(A, B//2)
    if B % 2:
        return (tmp * tmp % C) * A % C
    else:
        return tmp * tmp % C
    
result = split_vector(A, B)
print(result)
