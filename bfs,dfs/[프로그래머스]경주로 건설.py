from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

valueBoard = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방향과 value값을 계속해서 q에 넣어 가져가는게 핵심이다.
def bfs(x, y, car_d, value):
    q = deque()
    q.append((x, y, car_d, value))
    while q:
        x, y, car_d, value = q.popleft()
        for road_d in range(4):
            nx = x + dx[road_d]
            ny = y + dy[road_d]
            if -1 < nx < n and -1 < ny < n:
                if board[nx][ny] == 0:
                    if car_d == road_d or car_d == -1:
                        newValue = value + 100
                    else:
                        newValue = value + 600

                    if valueBoard[nx][ny] == 0:
                        valueBoard[nx][ny] = newValue
                        q.append((nx, ny, road_d, newValue))
                    else:
                        if valueBoard[nx][ny] >= newValue:
                            valueBoard[nx][ny] = newValue
                            q.append((nx, ny, road_d, newValue))


bfs(0, 0, -1, 0)
print(valueBoard[-1][-1])
