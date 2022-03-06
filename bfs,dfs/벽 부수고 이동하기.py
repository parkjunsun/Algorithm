# 미로탐색 변형문제

from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited[x][y][0] = 1
    while q:
        x, y, crash = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                #벽도 없고 그냥 갈 수 있는 경우
                if board[nx][ny] == 0 and visited[nx][ny][crash] == -1:
                    visited[nx][ny][crash] = visited[x][y][crash] + 1
                    q.append((nx, ny, crash))
                #벽이라서 한번은 뚫어도 되는 경우
                elif crash == 0 and board[nx][ny] == 1 and visited[nx][ny][1] == -1:
                    #crash가 0인걸 조건문에 넣은 이유는 crash가 만약 1이었다면 이미 한번 부셨다는건데 그런 경우는 걸러야 하니까 넣어준것
                    visited[nx][ny][1] = visited[x][y][crash] + 1
                    q.append((nx, ny, 1)) # 3번째 인자로 1을 넣어주면서 이미 벽을 한번 뚫었다는 표시를 해주는 것

bfs(0, 0)
ans1, ans2 = visited[n-1][m-1][0], visited[n-1][m-1][1]

if ans1 == -1 or ans2 != -1:
    print(ans2)
elif ans1 != -1 or ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))