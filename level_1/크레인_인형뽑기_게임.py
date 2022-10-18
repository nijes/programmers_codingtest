def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        # 인형 집기
        for i in range(len(board)):
            doll = board[i][move-1]
            if doll > 0:
                board[i][move-1] = 0
                break
        # 바구니에 넣기
        if len(basket) > 0 and doll == basket[len(basket)-1]:
            basket.pop()
            answer += 2
        elif doll != 0:
            basket.append(doll)
    return answer