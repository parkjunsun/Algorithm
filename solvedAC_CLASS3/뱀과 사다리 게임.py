from collections import deque

n, m = map(int, input().split())

ladder = []
snake = []
for _ in range(n):
    x, y = map(int, input().split())
    ladder.append((x, y))

for _ in range(m):
    u, v = map(int, input().split())
    snake.append((u, v))

def bfs(x, depth):
    q = deque()
    visited = [0] * 101
    q.append((x, depth))
    visited[x] = 1

    while q:
        x, depth = q.popleft()
        if x == 100:
            return depth

        for i in range(1, 7):
            nx = x + i
            for item in ladder:
                if nx == item[0]:
                    nx = item[1]
                    if visited[nx] == 0:
                        visited[nx] = 1
                        q.append((nx, depth+1))
                        break
            for item in snake:
                if nx == item[0]:
                    nx = item[1]
                    if visited[nx] == 0:
                        visited[nx] = 1
                        q.append((nx, depth+1))
                        break
            if nx <= 100:
                if visited[nx] == 0:
                    visited[nx] = 1
                    q.append((nx, depth+1))

print(bfs(1, 0))