from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

pieces_pos = []
pieces_pos2 = []


def solution(game_board, table):
    n = len(game_board)

    visited = [[0] * n for _ in range(n)]
    visited2 = [[0] * n for _ in range(n)]

    pieces = []
    pieces2 = []

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and table[i][j] == 1:
                bfs(i, j, visited, table)
            if visited2[i][j] == 0 and game_board[i][j] == 0:
                bfs2(i, j, visited2, game_board)

    for item in pieces_pos:
        l, t, r, b = int(1e9), int(1e9), -1, -1
        arr = []
        for pos in item:
            l, r = min(pos[1], l), max(pos[1], r)
            t, b = min(pos[0], t), max(pos[0], b)
        for pos in item:
            arr.append((pos[0] - t, pos[1] - l))
        new_piece = [[1] * (r - l + 1) for _ in range(b - t + 1)]

        for i in range(len(arr)):
            new_piece[arr[i][0]][arr[i][1]] = 0
        pieces.append(new_piece)

    for item in pieces_pos2:
        l, t, r, b = int(1e9), int(1e9), -1, -1
        arr = []
        for pos in item:
            l, r = min(pos[1], l), max(pos[1], r)
            t, b = min(pos[0], t), max(pos[0], b)
        for pos in item:
            arr.append((pos[0] - t, pos[1] - l))
        new_piece = [[1] * (r - l + 1) for _ in range(b - t + 1)]

        for i in range(len(arr)):
            new_piece[arr[i][0]][arr[i][1]] = 0
        pieces2.append(new_piece)

    all = []
    for piece in pieces:
        save = []
        save.append(piece)
        count = 0
        for item in piece:
            count += item.count(0)
        for i in range(3):
            new_piece = rotate_90(save[-1])
            if new_piece not in save:
                save.append(new_piece)
        all.append((save, count))

    ans = 0
    for piece in pieces2:
        for item in all:
            if piece in item[0]:
                ans += item[1]
                all.remove(item)
                break

    return ans


def bfs(x, y, visited, table):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    tmp = []

    while q:
        x, y = q.popleft()
        tmp.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < len(table) and -1 < ny < len(table):
                if visited[nx][ny] == 0 and table[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    pieces_pos.append(tmp)


def bfs2(x, y, visited, game_board):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    tmp = []

    while q:
        x, y = q.popleft()
        tmp.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < len(game_board) and -1 < ny < len(game_board):
                if visited[nx][ny] == 0 and game_board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    pieces_pos2.append(tmp)


def rotate_90(piece):
    r = len(piece)
    c = len(piece[0])

    new_piece = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            new_piece[j][r - i - 1] = piece[i][j]

    return new_piece


print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))