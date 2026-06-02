def solution(s):
    answer = []
    
    s = s[1:-2]
    
    s = s.split('},')
    
    data = []
    for i in s:
        temp = i[1:]
        data.append(list(map(int, temp.split(','))))
    
    data = sorted(data, key=len)

    temp = set()

    for item in data:
        diff = list(set(item) - temp)
        answer.append(diff[0])
        temp = set(item)

    return answer