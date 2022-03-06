from collections import deque

n = int(input())
visited = [[0] * (n+1) for _ in range(n+1)]

def bfs(screen,board, depth):
    q = deque()
    q.append((screen, board, depth))
    visited[screen][board] = 1

    while q:
        screen, board, depth = q.popleft()
        if screen == n:
            return depth

        if visited[screen][screen] == 0:
            visited[screen][screen] = 1
            q.append((screen, screen, depth+1))

        if screen + board <= n and visited[screen+board][board] == 0:
            visited[screen+board][board] = 1
            q.append((screen+board, board, depth+1))

        if screen - 1 >= n and visited[screen-1][board] == 0:
            visited[screen-1][board] = 1
            q.append((screen-1, board, depth+1))


print(bfs(1, 0, 0))