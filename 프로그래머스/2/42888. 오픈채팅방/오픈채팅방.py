def solution(record):
    users = dict()
    output = []
    
    for stats in record:
        detail = stats.split()
        if detail[1] not in users:
            users[detail[1]] = ""
        
        if detail[0] == 'Enter':
            users[detail[1]] = detail[2]
            output.append(f"{detail[1]} Enter")
        elif detail[0] == 'Leave':
            output.append(f"{detail[1]} Leave")
        elif detail[0] == 'Change':
            users[detail[1]] = detail[2]
    
    answer = []
    
    for msg in output:
        uid, act = msg.split()
        if act == 'Enter':
            answer.append(f"{users[uid]}님이 들어왔습니다.")
        elif act == 'Leave':
            answer.append(f"{users[uid]}님이 나갔습니다.")
    
    return answer