def solution(survey, choices):
    one_1 = 0 # 양수면 R, 음수면 T
    two_2 = 0 # 양수면 C, 음수면 F
    tre_3 = 0 # 양수면 J, 음수면 M
    fou_4 = 0 # 양수면 A, 음수면 N
    
    for i in range(len(survey)):
        if survey[i] == 'RT':
            if choices[i] > 4: # T
                one_1 -= (choices[i] - 4)
            else: # R
                one_1 += (4 - choices[i])
        elif survey[i] == 'TR':
            if choices[i] > 4: # R
                one_1 += (choices[i] - 4)
            else: # T
                one_1 -= (4 - choices[i])
        elif survey[i] == 'FC':
            if choices[i] > 4: # C
                two_2 += (choices[i] - 4)
            else: # F
                two_2 -= (4 -choices[i])     
        elif survey[i] == 'CF':
            if choices[i] > 4: # F
                two_2 -= (choices[i] - 4)
            else: # C
                two_2 += (4 - choices[i])
        elif survey[i] ==  'MJ':
            if choices[i] > 4: # J
                tre_3 += (choices[i] - 4)
            else: # M
                tre_3 -= (4 - choices[i])
        elif survey[i] == 'JM':
            if choices[i] > 4: # M
                tre_3 -= (choices[i] - 4)
            else: # J
                tre_3 +=  (4 - choices[i])
        elif survey[i] == 'AN':
            if choices[i] > 4: # N
                fou_4 -= (choices[i] - 4)
            else: # A
                fou_4 += (4 - choices[i])
        elif survey[i] == 'NA':
            if choices[i] > 4: # A
                fou_4 += (choices[i] - 4)
            else: # N
                fou_4 -= (4 - choices[i])
    
    answer = ''
    
    if one_1 < 0:
        answer += 'T'
    else:
        answer += 'R'
    if two_2 < 0:
        answer += 'F'
    else:
        answer += 'C'
    if tre_3 < 0:
        answer += 'M'
    else:
        answer += 'J'
    if fou_4 < 0:
        answer += 'N'
    else:
        answer += 'A'
    return answer