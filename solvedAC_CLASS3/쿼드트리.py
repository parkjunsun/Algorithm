n = int(input())
board = []
for _ in range(n):
    board.append(list(map(str, input())))

result = []

def quad_tree(x, y, n):
    global result
    color = board[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != board[i][j]:
                result.append('(')
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                result.append(')')
                return
    result.append(color)  #재귀함수로 안들어가고 for문이 끝난다면 범위안에 값이 전부 같은 값이기 때문에 result에 append


quad_tree(0, 0, n)
print(''.join(result))