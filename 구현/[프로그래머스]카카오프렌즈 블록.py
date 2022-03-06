def solution(n, m, board):
    new_board = []
    for i in range(n):
        new_board.append(list(board[i]))
    answer = 0
    while True:
        flag = True
        remove_pos = []
        for i in range(n-1):
            for j in range(m-1):
                if new_board[i][j] != 'O':
                    if new_board[i][j] == new_board[i][j+1] == new_board[i+1][j] == new_board[i+1][j+1]:
                        remove_pos.append((i, j))
                        remove_pos.append((i, j+1))
                        remove_pos.append((i+1, j))
                        remove_pos.append((i+1, j+1))
                        flag = False
        if flag:
            break
        remove_pos = list(set(remove_pos))
        for pos in remove_pos:
            new_board[pos[0]][pos[1]] = 'O'

        for i in range(n-1, -1, -1):
            for j in range(m):
                if new_board[i][j] != 'O':
                    tmp = new_board[i][j]
                    x, y = i, j
                    nx = x + 1
                    ny = y
                    while True:
                        if nx >= n:
                            break
                        if new_board[nx][ny] != 'O':
                            break
                        else:
                            new_board[nx-1][ny] = 'O'
                            new_board[nx][ny] = tmp
                        nx += 1

    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 'O':
                answer += 1

    for i in range(n):
        for j in range(m):
            print(new_board[i][j], end=' ')
        print()
    print()

    return answer


print(solution(6, 6, ["ABCDEA", "FGHIJK", "LMNXPQ", "QRSTYV", "WXZRAS", "DGFEAS"]))