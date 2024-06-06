def solution(board, moves):
    baguni = []
    size = len(board)
    answer = 0
    
    for move in moves:
        for i in range(size):
            if board[i][move - 1] != 0:
                baguni.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
                
        if len(baguni) > 1:
            if baguni[-1] == baguni[-2]:
                answer += 2
                baguni.pop()
                baguni.pop()

    return answer