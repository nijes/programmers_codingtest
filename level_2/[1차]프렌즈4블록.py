def solution(m, n, board):
    answer = 0

    # 시계방향 90도 회전
    board = [''.join(board[c][r] for c in range(m - 1, -1, -1)) for r in range(n)]

    while True:
        # 지워지는 블럭 set로 저장
        del_block = set()
        for r in range(n - 1):
            for c in range(m - 1):
                if board[r][c] != '0' and board[r][c] == board[r][c + 1] and board[r][c] == board[r + 1][c] and \
                        board[r][c] == board[r + 1][c + 1]:
                    del_block.add((r, c))
                    del_block.add((r + 1, c))
                    del_block.add((r, c + 1))
                    del_block.add((r + 1, c + 1))

        # 지워지는 블럭 없으면 종료
        if len(del_block) == 0: return answer
        # 지워지는 블럭 있으면 정답에 갯수 추가
        answer += len(del_block)

        # 블럭 지우기(블럭 없으면 0)
        for block in del_block:
            board[block[0]] = board[block[0]][:block[1]] + '0' + board[block[0]][block[1] + 1:]

            # 빈 공간 채우기
        for r in range(m):
            board[r] = board[r].replace('0', '')
            board[r] = board[r] + '0' * (n - len(board[r]))

    return answer