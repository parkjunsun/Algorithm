from collections import deque
import sys

n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

visited = [[[0] * (k+1) for _ in range(m)]for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, crashed):
    q = deque()
    q.append((x, y, crashed))
    visited[x][y][crashed] = 1
    while q:
        x, y, crashed = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if board[nx][ny] == 0 and visited[nx][ny][crashed] == 0:
                    visited[nx][ny][crashed] = visited[x][y][crashed] + 1
                    q.append((nx, ny, crashed))
                elif crashed < k and board[nx][ny] == 1:  # 벽이고 아직 벽을 k번 부수지 않았다면
                    if visited[nx][ny][crashed + 1] == 0: # 현재 crashed된 벽에서 1개 더 추가했을때 아직 부수지 않았다면
                        visited[nx][ny][crashed + 1] = visited[x][y][crashed] + 1
                        q.append((nx, ny, crashed + 1)) # 벽 부순 실제 개수를 증가시켜줌

bfs(0, 0, 0)

visited[n-1][m-1].sort()

if visited[n-1][m-1].count(0) == k+1:
    print(-1)
else:
    for num in visited[n-1][m-1]:
        if num != 0:
            print(num)
            sys.exit()